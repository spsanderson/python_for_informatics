'''chapter 6 exercises and examples'''

fruit = 'banana'
letter = fruit[1]
print letter

letter = fruit[0]
print letter

length = len(fruit)
last = fruit[length - 1]
print last

# A while loop that will traverse through the variable `fruit`
index = 0
while index < len(fruit):
    letter = fruit[index]
    print letter
    index = index + 1

# Write a while loop that starts with the last character and goes
# backwards

index = len(fruit) - 1
while index >= 0:
    letter = fruit[index]
    print letter
    index = index - 1
    
# Use of a for loop to do the samething - note how much quicker
# this may not always be the case though
for char in fruit:
    print char 

# Printing slices of a variable    
s = 'Monty Python'
print s[0:5]
print s[6:13]

fruit = 'banana'
print fruit[:3] # the print just forces output to screen
print fruit[3:] # the print just forces output to screen
print fruit[3:3] # nothing will print with this
print fruit[:] # this is the same as `print fruit`

greeting = 'Hello World!'
new_greeting = 'J' + greeting[1:]
print new_greeting

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print 'There are ' +str(count) + ' a(s) in',word

def count(string, letter):
    count = 0
    for i in string:
        if i == letter:
            count = count + 1
    print count

# The `in` operator
'a' in 'banana'

def alpha(string):
    if string < 'banana':
        print 'Your word, ' + string + ', comes before banana'
    elif string > 'banana':
        print 'Your word, ' + string + ', comes after banana'
    else:
        print 'All right, bananas'

'a' in 'banana'
# The above will print True to the screen

stuff = 'Hello world'
print type(stuff)
print dir(stuff)

word = 'banana'
new_word = word.upper()
print new_word
index = word.find('a')
print index
index_2 = word.find('na')
print index_2
index_3 = word.find('na', 3)
print index_3

# Stripping out white space
line = ' Here we go '
print line
print line.strip()

# Startswith method
line = 'Please have a nice day'
print line
print line.startswith('Please')
print line.startswith('p')

# use of line.lower() and use of a mutli method call
line = 'Please have a nice day'
print line.startswith('p')
print line.lower()
print line.lower().startswith('p')

word = 'banana'
print word.count('a')

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print atpos
sppos = data.find(' ',atpos)
print sppos
host = data[atpos+1:sppos]
print host

# Format operations
camels = 42
print '%d' % camels
print 'I have spotted %d camels.' % camels
print 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')

string = 'X-DSPAM-Confidence: 0.8475'
s = string.find(' ')
print s
e = string.find('5')
print e
fnum = float(string[s+1:e+1])
print fnum, type(fnum)

