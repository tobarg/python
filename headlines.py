none = open('none.txt')
for preps in none:
    preps = preps.split()

inp = raw_input('Enter file name: ')
driver = open(inp)
counts = dict()
for lines in driver:
    lines = lines.lower()
    lines = lines.replace('-',' ').replace('"','').replace(":",'').replace('?','').replace(',','')
    if lines.find('mediaplanet') > 1: continue
    else:
        words = lines.split()
        for word in words:
            if word in preps: continue
            if len(word) <= 1: continue
            else:
                counts[word] = counts.get(word,0)+1

keywords = list()
for key,val in counts.items():
    keywords.append((val,key))

keywords.sort(reverse=True)
rank = 0
for val,key in keywords[:25]:
    rank = rank + 1
    print rank, key, 'x', val
