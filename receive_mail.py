import imaplib
import email
from email.header import decode_header
import os
import pathlib
import text_decoder
from datetime import datetime


# TODO 1 ask for path to save attachments
# TODO 2 create default folder to save attachments
# TODO 3 return data to variables
# TODO 4 clean and simplify code

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)


class GetMail:
    """Use this class to receive emails
    """

    def __init__(self, email="maagarmeda2020@gmail.com", password="tveumgbczwsjomok", imap_server="imap.gmail.com"):
        self.email = email
        self.password = password
        self.imap_server = imap_server
        self.imap = imaplib.IMAP4_SSL(imap_server)
        self.today = datetime.now().strftime("%Y%m%d")

    def get_mail(self, num_msg, save_to=None):
        self.imap.login(self.email, self.password)
        status, messages = self.imap.select("INBOX")
        N = num_msg
        messages = int(messages[0])

        for i in range(messages, messages - N, -1):
            res, msg = self.imap.fetch(str(i), "(RFC822)")
            for response in msg:
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

                        print("Subject:", subject)
                        print("From:", From)

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
                            except:
                                body = ""

                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                # print text/plain emails and skip attachments
                                print(body)
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
                                    print(filepath)
                                    try:
                                        open(filepath, "wb").write(part.get_payload(decode=True))
                                    except OSError:
                                        filename = text_decoder.decoding(filename)
                                        filepath = os.path.join(folder_name, filename)
                                        open(filepath, "wb").write(part.get_payload(decode=True))
                    else:
                        # extract content type of email
                        content_type = msg.get_content_type()
                        # get the email body
                        body = msg.get_payload(decode=True).decode()
                        print(f'received Messages{body}')
                        if content_type == "text/plain":
                            # print only text email parts
                            print(body)
                        if content_type == "text/html":
                            # if it's HTML, create a new HTML file and open it in browser
                            print(body)
                    print("=" * 10)


get_mail = GetMail()
get_mail.get_mail(3, "C:\\Users\\SergioY\\Documents\\scripts\\zz-myemails")
