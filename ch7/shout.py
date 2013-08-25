'''
This exercise will write a program that will read through a file
and print the contents of the file (line by line) all in upper case.
Executing the program will look as follows:

HERE IS SOME EXAMPLE TEXT 
THAT WILL BE PRINTED OUT 
WHEN THIS PROGRAM IS RUN
'''
fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print 'The file',fhand,'does not exist or could not be opened'
    exit()
    
for line in fhand:
    line = line.upper().rstrip()
    print line
