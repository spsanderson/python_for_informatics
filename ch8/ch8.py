'''
This is material for chapter 8, this material and chapter focuses on
lists
'''
# A list of four integers
X = [10, 20, 30, 40]
print 'A list of integers', X

# A list of strings
X = ['crunchy frog', 'ram bladder', 'lark vomit']
print 'A list of strings', X

# An example of a nested list
X = ['spam', 2.0, 5, [10, 20]]
print 'A nested list', X

# An empty list
X = []
print 'The empty list', X

# Assigning lists to variables
cheeses = ['Chedder', 'Edam', 'Gouda']
print 'A list of cheeses', cheeses

numbers = [17, 123]
print 'A list of numbers', numbers

empty = []
print 'The empty set', empty

# Lists are mutable
print cheeses[0]

# We can change things in the list
numbers = [17, 123]
print numbers
numbers[1] = 5
print numbers

# The IN operator works on a list
print 'Edam' in cheeses
print 'Brie' in cheeses

# Traversing through a list, looping through
for cheese in cheeses:
    print cheese
    
# Now lets update the numbers[] by applying a multiplication function to each
# element
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    print numbers[i]

# A FOR loop over an empty list never executes the body:
for x in empty:
    print 'This never happens'
    
A = [1, 2, 3]
B = [4, 5, 6]
C = A + B
print A
print B
print C
print [0] * 4
print A * 3

# Slicing a list
T = ['a', 'b', 'c', 'd', 'e', 'f']
print T
print T[1:3]
print T[:4]
print T[3:]
# As you will notice the following two mean exactly the samething
print T, T[:]

# We can use a slice operator to update multiple elements of a list at the
# same time
print T
T[1:3] = ['x', 'y']
print T

# Appending items to a list
T = ['a', 'b', 'c']
print T
T.append('d')
print T
# Using extend to extend a list with all the elements of another list to it
T1 = ['a', 'b', 'c']
print T1
T2 = ['d', 'e']
print T2
T1.extend(T2)
print T1

# Sorting items in a list
T = ['d', 'c', 'e', 'b', 'a']
print T
T.sort()
print T

# Deleting elements
T = ['a', 'b', 'c']
X = T.pop(1)
print T
print X

# OR
T = ['a', 'b', 'c']
del T[1]
print T

# OR
T = ['a', 'b', 'c']
T.remove('b')
print T

# OR removing more than one element using a slice
T = ['a', 'b', 'c', 'd', 'e', 'f']
del T[1:5]
print T

# Lists and functions on them
nums = [3, 41, 12, 9, 74, 15]
print len(nums)
print max(nums)
print min(nums)
print sum(nums)
print sum(nums)/len(nums)

# two functions that cause an average of inputed numbers to be calculated
total = 0
count = 0
while (True):
    inp = raw_input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1
    
average = total / count
print 'Average: ', average

numlist = list() # this creates an empty list where all the values go
while (True):
    inp = raw_input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
    
average = sum(numlist) / len(numlist)
print 'Average: ', average

# This will break the string S into its parts
S = 'spam'
T = list(S)
print T

S = 'pining for the fjords'
T = list(S)
print T
T = S.split()
print T

# We can use line.split() to get parts of lines in files as well
'''
The first variable created is fhand, this will hold the file that we 
open using the open() command. Next we create a for loop that takes
every line in fhand and rstrips the space off then says if the line does not
start with 'From ' then skip it, but the ones that do start that way split
the line which will split it into its parts and then select the 3rd word from
every line, which is words[2] because we start at 0
'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print words[2]

# This works because Python creates one string object that is reference by
# two variables
A = 'banana'
B = 'banana'
print A is B

# The above does not work with lists, when a list is created it is a distinct
# in python
A = [1, 2, 3]
B = [1, 2, 3]
print A is B

# To get around this sort of thing we can alias as follows
A = [1, 2, 3]
B = A
print B is A

# In general it's good to avoid aliasing
B[0] = 17
print A

# This function will delete the first element of a list
def delete_head(t):
    del t[0]
    
# Here is an example of the function at work
letters = ['a', 'b', 'c']
delete_head(letters)
print letters

# appending something to a list
t1 = [1, 2]
t2 = t1.append(3)
print t1
print t2

t3 = t1 + [3]
print t3
print t2 is t3

# The following function does not actually delet the head of a list
def bad_delete_head(t):
    t = t[1:]
'''
The slice operator creates a new list and the assignment makes t refer
to it, but none of that has any effect on the list that was passed as an
argument.
An alternative is to write a function that creates and returns a new 
list. For example, tail returns all but the first element of a list
'''
def tail(t):
    return t[1:]
# The above function leaves the original list unmodified.
letters = ['a', 'b', 'c']
rest = tail(letters)
print rest

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #print 'Debug:', words
    if len(words) == 0:
        continue
    if words[0] != 'From':
        continue
    print words[2]

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #print 'Debug:', words
    if len(words) > 0 and words[0] == 'From':
        print words[2]
    
