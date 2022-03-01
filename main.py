from mail import SendEmail

sender_mail = "maagarmeda2020@gmail.com"
password = "potkhpjwgvbxxkcy"

email = SendEmail(sender_mail, password)

# email.simple(to="sergioyahni2@gmail.com",
#              subject="You Got Mail 01",
#              body="This is a test mail",
#              )

"""
# sender_mail = "YOU@GMAIL.COM"
# password = "YOUR_PASSWORD"
#
# email = SendEmail(sender_mail, password)
#
"""
email.send_email(to=['sergioyahni@gmail.com'],
                 cc=['sergioyahni2@gmail.com', 'sergioyahni@gmail.com'],
                 body="I AM YOUR MESSAGE")
