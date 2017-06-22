def hello():
    return 'Hello!'

print hello()

x = 'Howdy!'

big = max(x)
print big
tiny = min(x)
print tiny
length = len(x)
print length 

def computepay(h,r):
    if h <= 40:
    	return h * r
    else:
        return (40 * r) + ( (h - 40) * r * 1.5) 

hrs = raw_input("Enter Hours: ")
h = float(hrs) 
rate = raw_input("Enter Rate: ")
r = float(rate)

print 'Pay', computepay(h,r) 