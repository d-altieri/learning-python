import requests
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'<{tag}> - {attrs}')

    def handle_endtag(self, tag):
        print(f'<{tag}>')

    def handle_data(self, data):
        print(data)


parser = MyHTMLParser()

parser.feed("""
"""
)
