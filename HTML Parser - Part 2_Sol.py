from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        num_of_line = len(data.split('\n'))
        if num_of_line > 1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        if data.strip():
            print(data)
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

parser = MyHTMLParser()

html_string = ""
for _ in range(int(input())):
    html_string += input().rstrip() + '\n'
    
parser.feed(html_string)
parser.close()