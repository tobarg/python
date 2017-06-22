#files 
try:
    input = raw_input('Enter the file name: ')
except: 
    print 'File cannot be opened:', file
    quit()
#file = open('mbox-short.txt')

print 'Party\nPeople'

file = open(input)
inp = file.read()
print 'Characters in File:', len(inp)

file = open(input)
count = 0
for line in file:
    count = count + 1
    line = line.strip()
    if not line.startswith('From:'):
        continue
    print line
print 'Line Count:', count

#assignment 7.2 0 Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
count = 0
total = 0
file = open(fname)
for line in file:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    else :
        count = count + 1
        colon = line.find(':')
        string = line[colon+1:]
        number = float(string)
        total = total + number
print 'Average spam confidence:', total / count