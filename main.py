from mail import SendEmail

sender_mail = "maagarmeda2020@gmail.com"
password = "tveumgbczwsjomok"

email = SendEmail(sender_mail, password)

email.simple(to="sergioyahni2@gmail.com",
             subject="You Got Mail 01",
             body="This is a test mail",
             )

"""
# sender_mail = "YOU@GMAIL.COM"
# password = "YOUR_PASSWORD"
#
# email = SendEmail(sender_mail, password)
#
# email.send_email(to="RECIPIENT", # List
#                  cc="CC", # List default=None
#                  bcc="BCC", # List default=None
#                  subject="SUBJECT", # str default=None
#                  body="YOUR MESSAGE", # # plain text default=None
#                  reach_body="YOUR HTML MESSAGE", # html default=None
#                  filename="PATH/TO/FILE" default=None
)
"""