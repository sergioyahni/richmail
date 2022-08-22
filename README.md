# richmail 2.0
**richmail** can be used to send and receive emails. includes an editor for rich html text. 

Some email providers, such as gmail restrict sending emails from external apps for reasons related to security
and privacy protection issues.
example: to use this app with a gmail account you should procure an App Password at:
*Google Account > Security > Signing in to Google*

Please consult with your email provider before you use this class.

## Class Send() 
    from mail.mail import Send

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
    from mail.mail import Recive

    receive = Receive(mail, password, imap_server=None)

**Method get_mail()**

This method returns a list of dictionaries.
Define full path to folder to store received attachements. 

    receive.get_mail(num_msg=number of messages to fetch, #int required
                    save_to="path/to/save/attachment # str optional)

##Class Editor()

    from mail.editor import Editor

    editor = Editor()

**Method rich_text()**

This method returns html enriched text following the commands stated at the text to enrich.

    text = """[H2]I Am a title
    Lorem ipsum dolor sit amet, [B]consectetur adipiscing elit[*B]. 
    [ULIST]    
    [ITEM]Fusce vehicula nunc 
    [ITEM]Eget ante commodo
    [ULIST]
    Eu tincidunt magna elementum. Nam massa urna, egestas vitae"""

    rich_text = editor.rich_text(text)
    
**List of Commands**

The following commands can be used when preparing the text for the editor: 

    Commands within a line of text:
    
    Bold: [B]some text[*B]

    Italics: [I]some text[*I]

    Underline: [U]some text[*U]

    Overline: [O]some text[*O]

    Line Through: [LT]some text[*LT]
    
    Underline + overline: [UO]some text[*UO]

    Small Caps: [SC]some text[*SC]

    Lists:
     <ul>: 
           [ULIST]
           [ITEM]Some Text
           [ITEM]Some Text
           [*ULIST]
     <ol>:
           [OLIST]
           [ITEM]Some Text
           [ITEM]Some Text
           [*OLIST]

    Tables:
        [TABLES]
        [ROW]Some text | Some text | Some text
        [ROW]Some text | Some text | Some text
        [ROW]Some text | Some text | Some text
        [*TABLE]

    Commands at the beginning of the line:
    Titles: [H1], [H2], [H3], [H4], [H4], [H5], [H6]

    Commands at the beginning of the text:
    Change text direction: [LTR], [RTL]


