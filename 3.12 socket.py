#network & socket
#domain name > ip address
#port 80 is http

import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('www.py4inf.com', 80))

#http://www.example.com/page.htm
#protocol + host + document (url)
#request response cycle: href
#>>> telnet www.dr-chuck.com 80
#>>> GET http://www.dr-chuck.com/page1.htm HTTP/1.0

sock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = sock.recv(512) #512 characters
    if (len(data) < 1):
        break
    print data
sock.close()

#urllib > compact code
import urllib
doc = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in doc:
    print line.strip()

count = dict()
for line in doc:
    words = line.split()
    for word in words:
        count[word] = count.get(word,0)+1
print count

#assignment 3.2
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('www.pythonlearn.com', 80))

sock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = sock.recv(512)
    if (len(data) < 1):
        break
    print data
sock.close()
