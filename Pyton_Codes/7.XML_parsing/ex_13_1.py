# example_1: http://py4e-data.dr-chuck.net/comments_42.xml
# example_2:  http://py4e-data.dr-chuck.net/comments_1282834.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
print('Retriving', address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
print('Count: ', len(results))
conta=list()
for i in results:
    conta.append(int(i.find('count').text))
print('Sum: ',sum(conta))
