from mail import Send, Receive

sender_mail = "maagarmeda2020@gmail.com"
password = "potkhpjwgvbxxkcy"
smtp_server="smtp.gmail.com"
server = "imap.gmail.com"
email = Receive(sender_mail, password, server)
e = email.get_mail(4, "C:\\Users\\SergioY\\Documents\\scripts\\zz-myemails")
print(e)

# email.simple(to="sergioyahni2@gmail.com",
#              subject="You Got Mail 01",
#              body="This is a test mail",
#              )

# email.send_email(to=['sergioyahni@gmail.com'],
#                  cc=['sergioyahni2@gmail.com', 'sergioyahni@gmail.com'],
#                  subject="You Got Mail",
#                  body="I AM YOUR MESSAGE 2")
