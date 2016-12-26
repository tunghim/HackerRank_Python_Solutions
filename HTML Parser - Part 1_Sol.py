from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        self.value(attrs)

    def handle_endtag(self, tag):
        print ("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        self.value(attrs)

    def value(self, attrs = None):
        if attrs:
            [print('->', attr, '>', val) for attr, val, in attrs]

parser = MyHTMLParser()
parser.feed('\n'.join([input() for _ in range(int(input()))]))