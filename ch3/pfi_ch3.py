5 == 5
# True
5 == 6
# False

x = 10
print x
if x%2 == 0:
	print 'x is even'
else:
	print 'x is odd'
print 'done'

x = 10
y = 9
if x < y:
	print 'x is less than y'
elif x > y:
	print 'x is greater than y'
else:
	print 'x is equal to y'
	
# A nested conditional statement
if x == y:
	print 'x and y are equal'
else:
	if x < y:
		print 'x is less than y'
	else:
		print 'x is greater than y'

# A nested condition boolean construct
x = 9
print 'x equals ' + str(x)
if 0 < x:
	if x < 10:
		print 'x is a positive single digit number'

# Catching exceptions using `try` and `except`
#     inp = raw_input('Enter Fahrenheit Temperature:')
#     fahr = float(inp)
#     cel = (fhar - 32.0) * 5.0 / 9.0
#     print cel
# The above code will fail and the program script will abort if
# something other than a number is put in. We can fix this by using
# a try and except statement to handle information that we are not
# looking for. We will have to comment out the above in order for the
# program to continue to execute otherwise it will fail since the 
# try / except statement is not available for use before the program
# blows up. The following will work:
inp = raw_input('Enter Fahrenheit Temperature:')
try:
	fahr = float(inp)
	cel = (fahr - 32.0) * 5.0 / 9.0
	print cel
except:
	print 'enter a number please'
	
import math
signal_power = 9.0
noise_power = 10.0
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print 'Decibels = ' + str(decibels)

