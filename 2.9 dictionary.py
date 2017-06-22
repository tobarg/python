#dictionaries

ddd = dict()
ddd['age']=25
ddd['year']=1988
print ddd
ddd['age']=23
print ddd

stuff = dict()
print stuff.get('candy',-1)

#read and split file faster
ob = open('ob2015.txt')
outbrain = ob.read()
words = outbrain.split()

counts = dict()

for word in words:
    word = word.lower()
    counts[word] = counts.get(word,0) + 1

words.sort()
#print words
#print counts.items()
print len(words), 'Words'
print len(outbrain), 'Characters'

#tuples 1.0
for key,val in counts.items():
    print val,key
    
#maxval and maxkey
maxkey = None
maxval = None
for key,val in counts.items():
    if maxval == None or maxval < val:
        maxkey = key
        maxval = val
print 'Top Word:', maxkey, maxval