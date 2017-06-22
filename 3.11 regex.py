#regular expresions > regex
# ^ beginning of line
# $ end of line
# . matches any character
# * repeats character 0 or more times
# + repeats character 1 or more times
# \s matches white space
# \S matches non-white space
# [] range. example: [0-9]
# findall() look for all instances
# when between () start/stop extraction
# when between [] means not

import re

doc = open('mbox-short.txt')
for line in doc:
    line = line.rstrip()
    if re.findall('^From',line):
        email = re.findall('@([^ ]*)',line)
        print email
#    elif re.findall('[0-9]+',line):
#        print line

#assignment 3.1
doc = open('regex_sum_281763.txt')

import re
total = 0

for line in doc:
    if re.search('[0-9]+',line):
        add = re.findall('[0-9]+',line)
        for val in add:
            val = int(val)
            total = total + val
print total
