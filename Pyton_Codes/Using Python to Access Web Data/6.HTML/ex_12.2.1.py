# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


# exemplo_1:http://py4e-data.dr-chuck.net/comments_42.html
# exemplo_final: http://py4e-data.dr-chuck.net/comments_1282832.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span') #name of the anchor tag - example: 'a', 'span'
lista=list()
for tag in tags:
    # Look at the parts of a tag
    #print(tag)
    #print(tag.string)
    tag=str(tag)
    number=re.findall('([0-9.]+)',tag)
    lista.append(int(number[0]))
    #print(number)
print(lista)
print(sum(lista))