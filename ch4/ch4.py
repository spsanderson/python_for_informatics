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

# Getting an item from a list at random
import random
t = [1, 2, 3]
print random.choice(t)

# Some math functions. First we have to import math so that python
# can make use of the math functions, math was already imported from 
# above.
print math

# signal_power and noise_power must first be defined
signal_power = 2
noise_power = 1
ratio = signal_power / noise_power
decibals = 10 * math.log10(ratio)
radians = 0.7
height = math.sin(radians)

degrees = 45
radians = degrees / 360.0 * 2 * math.pi 
math.sin(radians)
print "Ratio = " + str(ratio)
print "Decibals = " + str(decibals)
print "Height = " + str(height)
print "Sine of radians = " + str(math.sin(radians))
print""

# Defining a function
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."
    
print_lyrics()

# Calling a function inside a function, we wil call this one, 
# the_repeater()
def the_repeater():
    print_lyrics()
    print_lyrics()

the_repeater()

# A function that prints anything you type in twice, this one is like
# the_repeater() but it takes in a single parameter where the_repeater()
# takes no parameters.
def print_twice(a):
    print a
    print a
    
print_twice('steve')
print_twice(math.pi)

# An example of composition of a function
print_twice('Steven ' * 4)
print_twice(math.cos(math.pi))

x = math.cos(radians)
print x
golden = (math.sqrt(5) + 1) / 2
print golden

result = print_twice('bing')
print result
