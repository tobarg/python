outbrain = open('ob2015.txt')
keywords = list()
counts = dict()

for line in outbrain:
    line = line.rstrip()
    line = line.split()
    for word in line:
        word = word.lower()
        #replace characters
        word = word.replace('-',' ').replace('"','').replace(":",'').replace('?','').replace(',','')
        keywords.append(word)

keywords.sort()
print keywords

#count words - long method
for kw in keywords:
    if kw not in counts:
        counts[kw] = 1
    else:
        counts[kw] = counts[kw] + 1
#print counts

#count words - using get()
for kw in keywords:
    counts[kw] = counts.get(kw,0) + 1
for key in counts:
    print key, counts[key]

#tuple
#print counts.items()

top = list()
for keys,values in sorted(counts.items()):
    top.append((values,keys))
top.sort(reverse=True)
for values,keys in top[:20]:
    print values,keys

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print 'Top Word:',bigword, bigcount
