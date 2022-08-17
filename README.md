# richmail
**richmail 1.2.0.0** can be used to send and receive emails. 

Some email providers, such as gmail restrict sending emails from external apps for reasons related to security
and privacy protection issues.
example: to use this app with a gmail account you should procure an App Password at:
*Google Account > Security > Signing in to Google*

Please consult with your email provider before you use this class.

## Class Send() 

    send = Send(email="string", password="string", smtp_server=None)

**Method: send.simple()**
Send a plain text email to one or more recipients 
    send.simple(to=[list], subject=None, body=None)

**Method send.send_email()**

    send.send_email(to=[List],
                    cc="CC", # List, optional default=None
                    bcc="BCC", # List, optional default=None
                    subject="SUBJECT", # str, optional default=None
                    body="YOUR MESSAGE", # plain text, optional default=None
                    rich_body="YOUR HTML MESSAGE", # html, optional default=None
                    filename="PATH/TO/FILE" optional default=None)

## Class Receive()

    receive = Receive(mail, password, imap_server=None)

**Method get_mail()**

This method returns a list of dictionaries.
Define full path to folder to store received attachements. 

    receive.get_mail(num_msg=number of messages to fetch, #int required
                    save_to="path/to/save/attachment # str optional)
