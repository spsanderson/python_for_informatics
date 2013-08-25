'''
This exercise will write a program that will read through a file
and print the contents of the file (line by line) all in upper case.
Executing the program will look as follows:

HERE IS SOME EXAMPLE TEXT 
THAT WILL BE PRINTED OUT 
WHEN THIS PROGRAM IS RUN
'''
fhand = raw_input('Enter the file name: ')
try:
    fname = open(fhand)
except:
    print 'The file'fhand,'does not exist or could not be opened'
    exit()
