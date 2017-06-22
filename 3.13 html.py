#HTML parsing
#beautiful soup

import re
import urllib
from bs4 import BeautifulSoup

#url could be raw_input
url = urllib.urlopen('http://www.dr-chuck.com/page1.htm').read()
soup = BeautifulSoup(url, 'html.parser')
tags = soup('a')
link = dict()

for tag in tags:
    if tag in link:
        continue
    else:
        link[tag] = link.get('href', None)

print link

for tag in tags:
    print 'TAG:',tag
    print 'URL:',tag.get('href', None)
    print 'Content:',tag.contents[0]
    print 'Attrs:',tag.attrs

#assignment scraping
import urllib
from bs4 import BeautifulSoup

doc = urllib.urlopen('http://python-data.dr-chuck.net/comments_281768.html').read()

soup = BeautifulSoup(doc, 'html.parser')
span = soup('span')

total = 0
for line in span:
    line = str(line)
    add = re.findall('([0-9]+)',line)
    for val in add:
        val = int(val)
        total = total + val

print total

#assignment following
import urllib
from bs4 import BeautifulSoup

pos = 18
count = 7

url = 'http://python-data.dr-chuck.net/known_by_Jiayi.html'

for i in xrange(count):
    url = urllib.urlopen(url).read()
    soup = BeautifulSoup(url, 'html.parser')
    hrefs = soup('a')
    url = hrefs[pos-1].get('href',None)

print hrefs[pos-1].contents[0]
