from mail import Send, Receive

email="maagarmeda2020@gmail.com"
password="tveumgbczwsjomok"
imap_server="imap.gmail.com"


email = Receive(email, password, imap_server=imap_server)
e = email.get_mail(10,"C:\\Users\\SergioY\\Documents\\scripts\\zz-myemails")
print(e)