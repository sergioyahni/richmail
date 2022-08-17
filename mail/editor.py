class Html:
    ltr = '<!DOCTYPE html><html dir="ltr"><head><meta charset="UTF-8">'
    rtl = '<!DOCTYPE html><html dir="rtl"><head><meta charset="UTF-8">'
    head = """<style>* {margin: 0;padding: 0;box-sizing: border-box;}body {width: 80%;margin: 2%;}html, body, div, 
    h1, h2, h3, h4, h5, h6, p, span{font-family: Arial, Helvetica, sans-serif;}h1, h2, h3, h4, h5, h6, p{margin-top: 1em;}.bold{font-weight: 900;}.italics{font-style: italic;}.underline{text-decoration: 
    underline;}.overline{text-decoration: overline;}.line-through{text-decoration: line-through;}.underline-overline{
    text-decoration: underline overline;}.small-caps{font-variant: small-caps;}</style><title></title>"""
    body = '<body>'
    footer = '</body></html>'


class Editor(Html):
    """
    This class returns formatted text:

    Commands within a line of text:
    Bold: [B]some text[*B]
    Italics: [I]some text[*I]
    Underline: [U]some text[*U]
    Overline: [O]some text[*O]
    Line Through: [LT]some text[*LT]
    Underline + overline: [UO]some text[*UO]
    Small Caps: [SC]some text[*SC]

    Commands at the beginning of the line:
    Titles: [H1], [H2], [H3], [H4], [H4], [H5], [H6]

    Commands at the beginning of the text:
    Change text direction: [LTR], [RTL]

    """
    def rich_text(self, text=None):
        edited = list()
        for line in text.splitlines():
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

            edited.append(line)
        content = ''.join(edited) + self.footer

        body_content = self.head + self.body + content

        if text[:5] == '[RTL]':
            rich_body = body_content.replace('[RTL]', '')
            rich_body = rich_body.replace('<body>', '<body dir="rtl">')
            rich_body = self.rtl + rich_body
        elif text[:5] == '[LTR]':
            rich_body = body_content.replace('[LTR]', '')
            rich_body = rich_body.replace('<body>', '<body dir="ltr">')
            rich_body = self.ltr + rich_body
        else:
            rich_body = self.ltr + body_content
        return rich_body


if __name__ == "__main__":
    my_text = ""

    html = Editor()
    res = html.rich_text(my_text)
    print(res)
