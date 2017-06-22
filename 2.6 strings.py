#strings
print "Start"

fruit = 'banana'
letter = fruit[5]
print letter
n = len(fruit)
w = fruit[n - 1]
print n

for letter in fruit:
    print letter

count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1
print count

word = 'Monty Python'
print word[0:4]
print word[6:]
print word[:]

#string methods
print word.lower()
print word.upper()
print word.find('y')
print word.replace('Py','Omega')
print word.replace('o','a')

#stripping spaces
print word.lstrip()
print word.rstrip()
print word.strip()

print 'Domain Search'
data = 'from tobiasdelfa@gmail.com sat jan 8, 2016'
at = data.find('@')
sp = data.find(' ',at)
domain = data[at + 1 : sp]
print domain

#assignment
text = "X-DSPAM-Confidence:    0.8475";
colon = text.find(':')
number = text[colon+1 :]
print float(number)
