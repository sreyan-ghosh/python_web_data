import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_933550.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

file = urllib.request.urlopen(url, context=ctx)
xml = file.read()
tree = ET.fromstring(xml)
nos = tree.findall('.//count')
print('Number of numbers: ', len(nos))
sum = 0
for item in nos:
    sum += int(item.text)
print(sum)