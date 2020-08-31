import ssl
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# To ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# using BS to extract the html content
url = input('Enter URL - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# extracting the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))