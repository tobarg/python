#tuples
#tuples are like lists but "immutable"
#tuples can be indexed starting at 0
#tuples cannot sorted, appended, reversed
#tuples are good for "temporary" variables that wont change

#tuples are comparable > < =
#you can sort a list of tuples!

#top 10
outbrain = open('ob2015.txt')
counts = dict()
for line in outbrain:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

keywords = list()
for key,val in counts.items():
    keywords.append((val,key))

keywords.sort(reverse=True)

for val,key in keywords[:10]:
    print val,key

#top shorter
random = {'a':10,'b':4,'c':19,'d':13}
print sorted( [ (v,k) for k,v in random.items() ] )

#assignment v2
handle = open('mbox-short.txt')
lst = list()

for line in handle:
    if not line.startswith('From '):
        continue
    else:
        string = line.split()
        hhmmss = string[5]
        hh = hhmmss.split(':')
        hour = hh[0]
        lst.append(hour)

counts = dict()
for days in lst:
    counts[days] = counts.get(days,0) + 1

dayz = list()
for k,v in counts.items():
    dayz.append((k,v))
dayz.sort()

for d,n in dayz:
    print d,n
