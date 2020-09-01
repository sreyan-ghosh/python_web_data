import json, ssl
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_933551.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

file = urllib.request.urlopen(url, context=ctx)
data = file.read()
json = json.loads(data)
sum = 0
for item in json['comments']:
    sum += int(item['count'])
print(sum)