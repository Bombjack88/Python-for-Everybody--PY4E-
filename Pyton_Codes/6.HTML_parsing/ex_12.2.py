# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
lista=list()
for tag in tags:
    # Look at the parts of a tag
    lista.append(int(tag.string))
    #print('span', tag)
    #print('span', tag.get('span', None))
    #print('span', tag.contents[0])
    #print('span', tag.attrs)
print(lista)
print(sum(lista))