x = 10
while True: 
    if x >= 2:
        print x
        x = x - 2
        continue
    else: 
        break
print x

largest_so_far = -1
for i in [10, 9, 16, 13, 21, 4]:
    if i > largest_so_far:
        largest_so_far = i 
    print largest_so_far, i
print 'End'

smallest = None
for number in [10, 9, 16, 13, 21, 4]:
    if smallest is None:
        smallest = number
    elif number < smallest: 
        smallest = number
    print smallest, number
print 'End'


# assignment 5.2 
largest = None
smallest = None

while True:
	try:
		num = raw_input("Enter a number: ")
		if num == "done": break 
		n = int(num)

#program for largest and smallest
		if largest is None:
			largest = n
			smallest = n 
		elif n > largest:
			largest = n
		elif n < smallest:
			smallest = n 

		continue
	except: 
		print "Invalid input"
        continue 
        
print "Maximum is", largest
print "Minimum is", smallest 