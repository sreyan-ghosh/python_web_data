import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup # web scraping library

url = 'http://www.dr-chuck.com/page-1.htm'
filehand = urllib.request.urlopen(url)
html = filehand.read()
soup = BeautifulSoup(html, 'html.parser') # read up on BS documentation for more

tags = soup('a') # gets all anchor tag objects in a list
for tag in tags:
    print(tag.get('href', None)) # gets the href component of the anchor object