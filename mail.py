import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail:
    """This class control sending emails. You can send plain and formatted text emails. Emails may include attachments.
    Some email providers, such as gmail restrict sending emails from external apps for reasons related to security
    and privacy protection issues.
    For example: to use this app with a gmail account you should procure an App Password at:
    Google Account > Security > Signing in to Google

    Please consult with your email provider before you use this class.

    email = SendEmail(your_address@email.com, your_password)
    email.send_email(to="RECIPIENT", # List, required
                   cc="CC", # List, optional default=None
                   bcc="BCC", # List, optional default=None
                   subject="SUBJECT", # str, optional default=None
                   body="YOUR MESSAGE", # plain text, optional default=None
                   reach_body="YOUR HTML MESSAGE", # html, optional default=None
                   filename="PATH/TO/FILE" optional default=None
)

    """
    def __init__(self, email, password, smtp_server="smtp.gmail.com"):
        self.smtp_server = smtp_server
        self.port = 587
        self.context = ssl.create_default_context()

        self.from_email = email
        self.password = password
        self.to_email = list()
        self.cc_mail = list()
        self.bcc_mail = list()
        self.message = ''

    def simple(self, to_email, subject=None, body=None):
        """Use this method to send plain text mails. requires at least one recipient email:
        email.simple(to=RECIPIENT # list, required
                 subject=SUBJECT # str, optional
                 body=MESSAGE, # str, optional
                 )
        """
        self.message = f'subject:{subject}\n\n{body}'
        self.to_email = ','.join(to_email)
        self._send()

    def send_email(self, **mail):
        # Create a multipart message and set headers
        message = MIMEMultipart()
        self.to_email = mail["to"]
        message["From"] = self.from_email
        message["To"] = ','.join(mail["to"])
        if "subject" in mail:
            message["Subject"] = mail["subject"]
        if "cc" in mail:
            self.cc_mail = mail["cc"]
            message["CC"] = ','.join(mail["cc"])

        if "bcc" in mail:
            self.bcc_mail = mail["bcc"]
            message["Bcc"] = ','.join(mail["bcc"])


        # Add body to email
        if "body" in mail:
            message.attach(MIMEText(mail["body"], "plain"))

        if "reach_body" in mail:
            message.attach(MIMEText(mail["reach_body"], "html"))

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
        try:
            self.to_email = self.to_email + self.cc_mail + self.bcc_mail
            server = smtplib.SMTP(self.smtp_server, self.port)
            server.ehlo()  # Can be omitted
            server.starttls(context=self.context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(self.from_email, self.password)
            server.sendmail(self.from_email, self.to_email, self.message)
        except Exception as e:
            # Print any error messages to stdout
            print(f'ERROR: {e}')
        finally:
            server.quit()
