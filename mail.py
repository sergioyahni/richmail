import email
import imaplib
import os
import smtplib
import ssl
from datetime import datetime
from email import encoders
from email.header import decode_header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from text_functions import clean, decoding


class User:
    """This class control the user and is inherited by the Send() and Receive() classes.
    Initialize:

    User(email="string", password="string", smtp_server=None, imap_server=imap_server)

    Some email providers, such as gmail restrict sending emails from external apps for reasons related to security
    and privacy protection issues.
    For example: to use this app with a gmail account you should procure an App Password at:
    Google Account > Security > Signing in to Google
    Please consult with your email provider before you use this class.
    """
    def __init__(self, mail, password, smtp_server=None, imap_server=None):
        self.user_email = mail
        self.password = password
        self.smtp_server = smtp_server
        self.imap_server = imap_server


class Send(User):
    """This class control sending emails. You can send plain and formatted text emails. Emails may include attachments.

    send = Send(email="string", password="string", smtp_server=None)

    send.simple(to=[list], subject=None, body=None)

    send.send_email(to=[List],
                    cc="CC", # List, optional default=None
                    bcc="BCC", # List, optional default=None
                    subject="SUBJECT", # str, optional default=None
                    body="YOUR MESSAGE", # plain text, optional default=None
                    reach_body="YOUR HTML MESSAGE", # html, optional default=None
                    filename="PATH/TO/FILE" optional default=None
)

    """
    port = 587
    context = ssl.create_default_context()
    to_email = list()
    cc_mail = list()
    bcc_mail = list()
    message = ''

    def simple(self, to, subject=None, body=None):
        """email.simple(to=RECIPIENT # list, required
                        subject=SUBJECT # str, optional
                        body=MESSAGE, # str, optional)
        """
        self.message = f'subject:{subject}\n\n{body}'
        if not isinstance(to, list):
            raise TypeError("A list is expected.")
        self.to_email = ','.join(to)
        self._send()

    def send_email(self, **mail):
        """email.send_email(to="RECIPIENT", # List, required
                   cc="CC", # List, optional default=None
                   bcc="BCC", # List, optional default=None
                   subject="SUBJECT", # str, optional default=None
                   body="YOUR MESSAGE", # plain text, optional default=None
                   reach_body="YOUR HTML MESSAGE", # html, optional default=None
                   filename="PATH/TO/FILE" optional default=None)
        """
        message = MIMEMultipart()
        if not isinstance(mail['to'], list):
            raise TypeError('"To" argument should be of list type')
        self.to_email = mail["to"]
        message["From"] = self.user_email
        message["To"] = ','.join(mail["to"])
        if "subject" in mail:
            message["Subject"] = mail["subject"]
        if "cc" in mail:
            if not isinstance(mail['cc'], list):
                raise TypeError('"cc" argument should be of list type')
            self.cc_mail = mail["cc"]
            message["CC"] = ','.join(mail["cc"])

        if "bcc" in mail:
            if not isinstance(mail['bcc'], list):
                raise TypeError('"bcc" argument should be of list type')
            self.bcc_mail = mail["bcc"]
            message["Bcc"] = ','.join(mail["bcc"])

        # Add body to email
        if "body" in mail:
            message.attach(MIMEText(mail["body"], "plain"))

        if "rich_body" in mail:
            message.attach(MIMEText(mail["rich_body"], "html"))

        if "filename" in mail:
            filename = mail["filename"]

            # Open file in binary mode
            with open(filename, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # Add attachment to message and convert message to string
            message.attach(part)
        self.message = message.as_string()
        self._send()

    def _send(self):
        if not self.smtp_server:
            raise Exception ("SMTP server was not defined")
        if self.cc_mail or self.bcc_mail:
            self.to_email = self.to_email + self.cc_mail + self.bcc_mail
        server = smtplib.SMTP(self.smtp_server, self.port)
        server.ehlo()  # Can be omitted
        server.starttls(context=self.context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(self.user_email, self.password)
        server.sendmail(self.user_email, self.to_email, self.message)
        server.quit()


class Receive(User):
    """This class controls receiving emails

    receive = Receive(mail, password, imap_server=None)

    receive.get_mail(num_msg=number of messages to fetch, #int required
                    save_to="path/to/save/attachment # str optional)
    """

    today = datetime.now().strftime("%Y%m%d_%H%M%S")
    received_emails = list()

    def get_mail(self, num_msg, save_to=None):
        # imap_server = self.imap_server
        if not self.imap_server:
            raise Exception("IMAP sever was not defined")
        imap = imaplib.IMAP4_SSL(self.imap_server)
        imap.login(self.user_email, self.password)
        status, messages = imap.select("INBOX")
        N = num_msg
        messages = int(messages[0])

        for i in range(messages, messages - N, -1):
            res, msg = imap.fetch(str(i), "(RFC822)")
            for response in msg:
                single = dict()
                if isinstance(response, tuple):
                    # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])

                    # decode the email subject
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        # if it's a bytes, decode to str
                        try:
                            subject = subject.decode(encoding) if encoding else subject
                        except LookupError as err:
                            subject = err

                    # decode email sender
                    From, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(From, bytes):
                        try:
                            From = From.decode(encoding) if encoding else From
                        except LookupError as err:
                            From = err

                        single['subject'] = subject
                        single['from'] = From

                    # if the email message is multipart
                    if msg.is_multipart():
                        # iterate over email parts
                        for part in msg.walk():
                            # extract content type of email
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                # get the email body
                                body = part.get_payload(decode=True).decode()
                            except AttributeError:
                                body = ""
                            except UnicodeDecodeError:
                                body = ""

                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                single['body'] = body
                            elif "attachment" in content_disposition:
                                # download attachment
                                filename = part.get_filename()
                                if filename:
                                    folder_name = clean(subject)
                                    folder_name = self.today if not folder_name else folder_name
                                    folder_name = folder_name if not save_to else f'{save_to}/{folder_name}'
                                    if not os.path.isdir(folder_name):
                                        # make a folder for this email (named after the subject)
                                        os.mkdir(folder_name)
                                    filepath = os.path.join(folder_name, filename)
                                    # download attachment and save it
                                    single['attachment'] = filepath
                                    try:
                                        open(filepath, "wb").write(part.get_payload(decode=True))
                                    except OSError:
                                        filename = decoding(filename)
                                        filepath = os.path.join(folder_name, filename)
                                        open(filepath, "wb").write(part.get_payload(decode=True))
                    else:
                        # extract content type of email
                        content_type = msg.get_content_type()
                        # get the email body
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            single['body'] = body
                        if content_type == "text/html":
                            single['body'] = body
                if single:
                    self.received_emails.append(single)
        return self.received_emails
