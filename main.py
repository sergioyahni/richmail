import config
from mail.mail import Send
from mail.editor import Editor
from report import text

send = Send(mail=config.email, password=config.psw, smtp_server=config.smtp)
content = Editor()


send.send_email(to=["sergioy@tourism.gov.il"],
                subject="This report may interest you",  # str, optional default=None
                rich_body=content.rich_text(text),  # html, optional default=None
                )
