import config
from mail.mail import Send
from mail.editor import Editor

send = Send(mail=config.email, password=config.psw, smtp_server=config.smtp)
content = Editor()

my_text = """
    [H3]malesuada massa posuere
    Lorem ipsum [B]dolor sit amet[*B], consectetur adipiscing elit. Suspendisse elementum sem diam, 
    a sodales tellus luctus in. Nunc eu purus ut erat placerat ullamcorper nec at nisi. Nullam pulvinar erat nunc, 
    at consectetur lorem maximus ut. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac 
    turpis egestas. Proin aliquet, nibh id scelerisque vulputate, metus mauris scelerisque odio, vel molestie risus 
    neque quis justo. Nam consequat a quam at faucibus. Sed pretium sem nec sem dictum: https://google.com, vel porta mauris semper. 
    Suspendisse non eros posuere, [LT]consectetur quam nec[*LT], condimentum orci. [U]Aenean ultricies tellus sem[*U], 
    in luctus augue hendrerit ac. Duis eget varius nibh, id mollis nibh. Praesent hendrerit enim accumsan magna 
    porta, vel dignissim erat faucibus. Quisque vehicula elit ac tortor molestie faucibus. Etiam vel condimentum 
    tellus. Donec at augue ut arcu lobortis volutpat. Maecenas quis mauris eget libero commodo molestie. Integer ac 
    nunc malesuada massa posuere placerat et ut massa.
    
     [UO]this is a very interesting line[*UO]
    """
print(content.rich_text(my_text))

# text2 = """[RTL]
# ו"ר הרשות הפלסטינית אבו מאזן פרסם הבוקר (רביעי) הבהרה לאמירתו ולפיה "ישראל ביצעה 50 שואות בפלסטינים"
# במסיבת העיתונאים המשותפת אמש עם קנצלר גרמניה אולף שולץ, ואמר כי "השואה היא הפשע הנתעב ביותר שהתרחש בהיסטוריה המודרנית
# של האנושות. בתשובתו לא הייתה כוונה להתכחש לייחודיות של השואה, שבוצעה במאה הקודמת, והיא דבר שיש לגנות בחריפות". """
#
# send.send_email(to=["sergioyahni2@gmail.com"],
#                 subject="This one is in English",  # str, optional default=None
#                 rich_body=content.rich_text(my_text),  # html, optional default=None
#                 )
