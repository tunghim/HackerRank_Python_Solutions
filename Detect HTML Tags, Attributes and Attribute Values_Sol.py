from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.value(attrs)

    def value(self, attrs = None):
        for attr, val, in attrs:
            print('->', attr, '>', val)

parser = MyHTMLParser()
parser.feed('\n'.join([input() for _ in range(int(input()))]))