none = open('none.txt')
for preps in none:
    preps = preps.rstrip()
    preps = preps.split()

url = open('moat2015.txt')
counts = dict()

for lines in url:
    if len(lines)<50: continue
    else:
        lines = lines.rstrip()
        com = lines.find('.com/')
        web = lines[com+5:]
        slash = web.find('/')
        art = web[slash+1:]
        words = art.split('-')
        for word in words:
            word = word.lower()
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
