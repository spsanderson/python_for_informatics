# Chapter 5 exercises and problems
# The following statement will return an assignment error and is hence
# commented out

# x = x + 1

# We first need to initialize the variable in the following fashion:
x = 0
print x
x = x + 1
print x

# An example of a 'while' statement
n = 5
print "n = ",n
while n > 0:
    print n
    n = n - 1
print 'Blastoff!'

# An example of an infinite loop DO NOT RUN CODE
########################################################################
#  n = 10
#  while True:
#      print n,
#      n = n - 1
#  print 'Done!'
########################################################################

# An example of an infinite loop that will `break` when the user
# enters in a terminal statement
while True:
    line = raw_input('> ')
    if line == 'done':
        break
    print line
print 'Done!'

# An example of a loop with a `continue` statement in it
while True:
    line = raw_input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print line
print 'Done!'

# Using a for loop to go through a list of items
friends = ['Joseph', 'Pat', 'John']
for friend in friends:
    print 'Happy New Year:', friend
print 'Done!'

# Counting and summing loops
# Counting loop
count = 0
for i in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print 'There are',count,'items in the list and the'

# Summing loop
total = 0
for i in [3, 41, 12, 9, 74, 15]:
    total = total + i
print 'the total of those',count,'items is: ',total

# we could also use the len() function to get the length of the list
# and we could use the sum() function to get the total of the list

# Maximum and minumum loop function
largest = None
print 'Before:', largest
for i in [3, 41, 12, 9, 74, 15]:
    if largest is None or i > largest:
        largest = i
    print 'Loop:', i, largest
print 'Largest:', largest

# We can also accomplish the above using the max() function like so
biggest = max([3, 41, 12, 9, 74, 15])
print biggest

smallest = None
print 'Before:', smallest
for i in [3, 41, 12, 9, 74, 15]:
    if smallest is None or i < smallest:
        smallest = i
    print 'Loop:', i, smallest
print 'Smallest:', smallest

# We can also accomplish this by using the min() function like so
lowest = min([3, 41, 12, 9, 74, 15])
print lowest
