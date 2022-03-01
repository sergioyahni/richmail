import imaplib
import email
from email.header import decode_header
import os
import text_decoder

# account credentials
# username = "maagarmeda2020@gmail.com"
# password = "tveumgbczwsjomok"
# imap_server = "imap.gmail.com"


def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)


class GetMail:
    """Use this class to receive emails
    """
    def __init__(self,email="maagarmeda2020@gmail.com", password="tveumgbczwsjomok", imap_server="imap.gmail.com"):
        self.email = email
        self.password = password
        self.imap_server = imap_server
        self.imap = imaplib.IMAP4_SSL(imap_server)

    def get_mail(self, num_msg):
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
                        subject = subject.decode(encoding) if encoding else subject

                    # decode email sender
                    From, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(From, bytes):
                        From = From.decode(encoding) if encoding else From
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
# close the connection and logout
# imap.close()
# imap.logout()
get_mail = GetMail()
get_mail.get_mail(3)
