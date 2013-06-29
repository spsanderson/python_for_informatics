# This is an example of a function in python
# this function is user defined.
# A function is a bit of reusable code that
# takes arguments(s) as input and does something
# that we define and the result gets returned
# def  is used to tell python that we are making
# a function and it is something we defined.
def hello():
    print "Hello"
    print "Fun"

hello()
print "Zip"
hello()

# This will print out the biggest item in big
big = max('Hello world')
print big

# This will print out the smallest thing in tiny
tiny = min('Hello world')
print tiny

# Import the math module and print the sqrt of a num
import math
print "The math module was just imported"
print math.sqrt(25.0)

# A small hello function that makes use of a parameter
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print greet('en'),'Glenn'
print greet('es'),'Sally'
print greet('fr'),'Michael'

# An example of a two parameter function
# it is important to note that functions can have many
# parameters
def addtwo(a,b):
    added = a + b
    return added

x = addtwo(3,5)
print x


