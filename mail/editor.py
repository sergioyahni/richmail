class Html:
    ltr = '<!DOCTYPE html><html dir="ltr"><head><meta charset="UTF-8">'
    rtl = '<!DOCTYPE html><html dir="rtl"><head><meta charset="UTF-8">'
    head = """<style>* {margin: 0;padding: 0;box-sizing: border-box;}body {width: 80%;margin: 5%;}html, body, div, 
    h1, h2, h3, h4, h5, h6, p, span{font-family: Arial, Helvetica, sans-serif;}h1, h2, h3, h4, h5, h6, p, ul,ol, 
    table{margin-top: 1em;}.bold{font-weight: 900;}.italics{font-style: italic;}.underline{text-decoration: 
    underline;}.overline{ text-decoration: overline;}.line-through{text-decoration: 
    line-through;}.underline-overline{ text-decoration: underline overline;}.small-caps{font-variant: small-caps;}ul{ 
    list-style-type: square;}
    table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}tr:nth-child(even) {background-color: #dddddd;}</style><title></title>"""
    body = '<body>'
    footer = '</body></html>'


class Editor(Html):
    """
    This class returns formatted text:

    Use the following commands within a line of text:
    Bold: [B]some text[*B]
    Italics: [I]some text[*I]
    Underline: [U]some text[*U]
    Overline: [O]some text[*O]
    Line Through: [LT]some text[*LT]
    Underline + overline: [UO]some text[*UO]
    Small Caps: [SC]some text[*SC]

    Lists:
     <ul>: [ULIST]
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

    Use the following commands at the beginning of the line:
    Titles: [H1], [H2], [H3], [H4], [H4], [H5], [H6]

    Use the following commands at the beginning of the text:
    Change text direction: [LTR], [RTL]
    """
    text: str
    mail_body: str

    def rich_text(self, text=None):
        self.text = text
        self.mail_body = self.head + self.body + self.__format_lines() + self.footer
        self.mail_body = self.__format_dir()
        # self.mail_body = self.__format_lists()

        return self.mail_body

    def __format_dir(self):
        if self.text[:5] == '[RTL]':
            rich_body = self.mail_body.replace('[RTL]', '')
            rich_body = rich_body.replace('<body>', '<body dir="rtl">')
            rich_body = self.rtl + rich_body
        elif self.text[:5] == '[LTR]':
            rich_body = self.mail_body.replace('[LTR]', '')
            rich_body = rich_body.replace('<body>', '<body dir="ltr">')
            rich_body = self.ltr + rich_body
        else:
            rich_body = self.ltr + self.mail_body
        return rich_body

    def __format_lines(self):
        edited = list()
        for line in self.text.splitlines():
            line = '<p>' + line
            line = line.replace('[B]', '<span class="bold">')
            line = line.replace('[*B]', '</span>')
            line = line.replace('[I]', '<span class="italics">')
            line = line.replace('[*I]', '</span>')
            line = line.replace('[U]', '<span class="underline">')
            line = line.replace('[*U]', '</span>')
            line = line.replace('[O]', '<span class="overline">')
            line = line.replace('[*O]', '</span>')
            line = line.replace('[LT]', '<span class="line-through">')
            line = line.replace('[*LT]', '</span>')
            line = line.replace('[UO]', '<span class="underline-overline">')
            line = line.replace('[*UO]', '</span>')
            line = line.replace('[SC]', '<span class="small-caps">')
            line = line.replace('[*SC]', '</span>')
            line += '</p>'

            # Titles
            if line.find('[H1]') > 0:
                line = line.replace('[H1]', '')
                line = line.replace('<p>', '<h1>')
                line = line.replace('</p>', '</h1>')
            elif line.find('[H2]') > 0:
                line = line.replace('[H2]', '')
                line = line.replace('<p>', '<h2>')
                line = line.replace('</p>', '</h2>')
            elif line.find('[H3]') > 0:
                line = line.replace('[H3]', '')
                line = line.replace('<p>', '<h3>')
                line = line.replace('</p>', '</h3>')
            elif line.find('[H4]') > 0:
                line = line.replace('[H4]', '')
                line = line.replace('<p>', '<h4>')
                line = line.replace('</p>', '</h4>')
            elif line.find('[H5]') > 0:
                line = line.replace('[H5]', '')
                line = line.replace('<p>', '<h5>')
                line = line.replace('</p>', '</h5>')
            elif line.find('[H6]') > 0:
                line = line.replace('[H6]', '')
                line = line.replace('<p>', '<h6>')
                line = line.replace('</p>', '</h6>')
            else:
                pass

            # Unordered Lists
            if line.find('[ULIST]') > 0:
                line = line.replace('[ULIST]', '')
                line = line.replace('<p>', '<ul>')
                line = line.replace('</p>', '')
            if line.find('[ITEM]') > 0:
                line = line.replace('[ITEM]', '')
                line = line.replace('<p>', '<li>')
                line = line.replace('</p>', '</li>')
            if line.find('[*ULIST]') > 0:
                line = line.replace('[*ULIST]', '')
                line = line.replace('<p>', '</ul>')
                line = line.replace('</p>', '')
            # Ordered Lists
            if line.find('[OLIST]') > 0:
                line = line.replace('[OLIST]', '')
                line = line.replace('<p>', '<ol>')
                line = line.replace('</p>', '')
            if line.find('[ITEM]') > 0:
                line = line.replace('[ITEM]', '')
                line = line.replace('<p>', '<li>')
                line = line.replace('</p>', '</li>')
            if line.find('[*OLIST]') > 0:
                line = line.replace('[*OLIST]', '')
                line = line.replace('<p>', '</ol>')
                line = line.replace('</p>', '')

            # Tables
            if line.find('[TABLE]') > 0:
                line = line.replace('[TABLE]', '')
                line = line.replace('<p>', '<table>')
                line = line.replace('</p>', '')

            if line.find('[ROW]') > 0:
                line = line.replace('<p>', '')
                line = line.replace('</p>', '')
                line = line.replace('[ROW]', '')
                l0 = ['<tr>']
                l1 = line.split('|')
                for item in l1:
                    l0.append('<td>' + item + '</td>')
                line = ''.join(l0) + '</tr>'

            if line.find('[*TABLE]') > 0:
                line = line.replace('[*TABLE]', '')
                line = line.replace('<p>', '</table>')
                line = line.replace('</p>', '')

            edited.append(line)
        return ''.join(edited)


if __name__ == "__main__":
    my_text = """[H3]malesuada massa posuere
    Lorem ipsum [B]dolor sit amet[*B], consectetur adipiscing elit. Suspendisse elementum sem diam, 
    a sodales tellus luctus in. Nunc eu purus ut erat placerat ullamcorper nec at nisi. Nullam pulvinar erat nunc, 
    at consectetur lorem maximus ut. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac 
    turpis egestas. Proin aliquet, nibh id scelerisque vulputate, metus mauris scelerisque odio, vel molestie risus 
    neque quis justo. 
    [ULIST]
    [ITEM]Nam consequat a quam at faucibus. 
    [ITEM]Sed pretium sem nec sem dictum: https://google.com, vel porta mauris semper. 
    [*ULIST]
    [H2]Suspendisse non eros posuere
    [LT]consectetur quam nec[*LT], condimentum orci. [U]Aenean ultricies tellus sem[*U], 
    in luctus augue hendrerit ac. 
    [OLIST]
    [ITEM]Duis eget varius nibh, 
    [ITEM]id mollis nibh. 
    [ITEM]Praesent hendrerit enim accumsan magna 
    porta, 
    [*OLIST]
    vel dignissim erat faucibus. Quisque vehicula elit ac tortor molestie faucibus. Etiam vel condimentum 
    tellus. Donec at augue ut arcu lobortis volutpat. Maecenas quis mauris eget libero commodo molestie. Integer ac 
    nunc malesuada massa posuere placerat et ut massa.
    [TABLE]
    [ROW]vel dignissim erat faucibus | Quisque vehicula elit ac tortor | molestie faucibus 
    [ROW]Donec at augue ut arcu lobortis | 100 | 150 
    [ROW]Quisque vehicula elit | 300 | 350 
    [*TABLE]
    tellus. Donec at augue ut arcu lobortis volutpat. Maecenas quis mauris eget libero commodo molestie. Integer ac 
    nunc malesuada massa posuere placerat et ut massa.
    
     [UO]this is a very interesting line[*UO]"""

    html = Editor()
    # res = html.rich_text(my_text)
    with open('test1.html', "w", encoding='UTF-8') as f:
        f.write(html.rich_text(my_text))
