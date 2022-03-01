# SendMail
Use a GMAIL account to send mails. 

Import and initiate the Email class

**email = Email(sender_mail, password)**

Option 1: Send mail using the *simple* method - all arguments are mandatory: 

**email.simple("recipient's email", "email subject", "the body of the message")**

Option 2: Send mail using the *send_mail* method. Key "to" is a mandatory, all other keys are optionals. 

**email.send_email(to="RECIPIENT", cc="CC", bcc="BCC", subject="SUBJECT", body="YOUR MESSAGE", filename="PATH_TO_FILE")**

