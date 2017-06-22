#XML > serialization (wire protocol)
#serialization: creating wire format
#deserialize: convert wire format and create an internal structure
#organize next/tree levels using slashes: /a/b

#xml schema
#xs:element
#xs:sequence
#xs:complexType

#time format 2016-05-16T09:30:10Z
#Z stands for GMT/UTC

import xml.etree.ElementTree as ET

#triple quotes to open XML
data = '''
<person>
    <name>Chuck</name>
    <phone type='intl'>
        +1 917 655 0758
    </phone>
    <email hide='yes'/>
</person> '''
#triple quotes to close

tree = ET.fromstring(data)
print 'Name:', tree.find('name').text
print 'Attr:', tree.find('email').get('hide')

#assignment
import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_281765.xml'
www = urllib.urlopen(url).read()

tree = ET.fromstring(www)
counts = tree.findall('.//comment')

total = 0

for line in counts:
    line = line.find('.//count').text
    line = int(line)
    total = total + line

print total
