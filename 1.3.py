print 'Welcome!'

#input 
try:
	hours = raw_input('How many hours did you work? ')
	h = float(hours)
	rate = raw_input('What is your pay rate? ')
	r = float(rate)
except:
	print 'Please enter a valid number'
	quit() 

#conditionals
if h <= 40:
	print '$', h * r 
elif h <= 60:
	print '$', (40 * r) + ((h - 40) * r * 1.5)
else:
	print '$', (60 * r) + ((h - 60) * r * 2) 

print 'Enjoy your ca$h!'
	