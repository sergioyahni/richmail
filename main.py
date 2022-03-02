from mail import Send, Receive

email = "maagarmeda2020@gmail.com"
password = "tveumgbczwsjomok"
imap_server = "imap.gmail.com"
smtp_server = "smtp.gmail.com"

send = Send(email, password, smtp_server=smtp_server)
receive = Receive(email, password, imap_server=imap_server)
s = receive.get_mail(10,"C:\\Users\\SergioY\\Documents\\scripts\\zz-myemails")
print(s)

r = send.send_email(to=["sergioyahni@rmail.com"],
                    subject="An email with Attachments",
                    rich_body="<h2>Please download the attached file</h2><h3>Sergio</h3>",
                    filename="C:\\Users\\SergioY\\Documents\\webinars\\data\\LiveStreaming.xlsx")