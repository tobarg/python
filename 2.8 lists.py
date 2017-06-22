#lists
colors = ['red','yellow','blue','green']
numbers = [1,2,3,4,5]

print colors
print numbers

for color in colors:
    print 'Love', color

mix = colors + numbers
print mix
print mix[3:]

print 'Hate', colors[1].capitalize()
print len(colors)
print range(len(colors))

abc1 = 'every breath you take'
cut = abc1.split()
print cut

abc2 = 'every;smile;you;take'
cut2 = abc2.split(';')
print cut2

#sum
num = list()
while True:
    input = raw_input('enter a number: ')
    if input == 'done' : break
    value = float(input)
    num.append(value)
average = sum(num) / len(num)
print 'Total',sum(num)
print 'Average',average

#assignment 8.4 (finally)
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word in lst:
            continue
        else:
            lst.append(word)

lst.sort()
print lst
