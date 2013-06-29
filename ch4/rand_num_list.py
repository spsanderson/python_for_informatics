# This little program will retrun a list of random numbers
# It will ask for a number i, which is how many numbers
# that should be returned that fall between 0.0 and 1.0
import random

try:
    n = int(raw_input('How many numbers would you like?: \n'))
    print ''

except:
    print 'Please enter a valid number'
    quit()


for i in range(n):
    x = random.random()
    print x

print 'You just got ' + str(n) + ' random numbers'
