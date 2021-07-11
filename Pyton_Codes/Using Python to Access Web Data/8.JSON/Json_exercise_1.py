# example_1:  http://py4e-data.dr-chuck.net/comments_42.json
# example_2:  http://py4e-data.dr-chuck.net/comments_1282835.json

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
print('Retriving', address)
connection = urllib.request.urlopen(address, context=ctx)
data = connection.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
#print('Retrieved', len(info), 'characters')
#print('User count:', len(info))
#print(json.dumps(info, indent=2))
numbers=list()
count=0
for item in info['comments']:
    numbers.append(item['count'])
    #print('Conta', item['count'])
    count=count+1
print(f'Count: {count}')
print(f'SUM: {sum(numbers)}')