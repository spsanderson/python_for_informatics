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

