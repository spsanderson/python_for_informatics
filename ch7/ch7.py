'''Chapter 7 python for informatics code and exercises in this 
chapter we will start to open up files and work with them
in their current working directory. You can download a test
file at the following address:
http://www.py4inf.com/code/mbox.txt
'''
# We will open a file called mbox.txt which is in the director
# Dropbox/python_for_informatics/ch7
#fhand = file handle
fhand = open('mbox.txt')
print fhand

# New lines
stuff = 'Hello\nWorld'
print stuff

stuff = 'x\ny'
print stuff
print len(stuff)

# We will now count the lines in the file that we open, we will use
# fhand from above
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print 'Line count of file:',count

fhand = open('mbox-short.txt')
inp = fhand.read()
print len(inp)
print inp[:20]

fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print line
        
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print line

# The following code will do exactly the same as above
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    # skip uninteresting lines
    if not line.startswith('From:'):
        continue
    # Process interesting lines
    print line
    
# Making use of find()
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue
    print line


# The following will allow a user to specify a particular file name
# providing it is in the same working directory as the python file
# itself
fname = raw_input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print 'There were',count,'subject lines in',fname

# Now we will construct a block of code to do the same exact thing
# only now we will use a try/except block incase a user inputs a file
# that does not exist in the cwd (current working directory)
fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print 'The file:',fname,', could not be found or opened'
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print 'There were',count,'subject lines in',fname

# Writing files with 'w' we will use fout = file out. If the file 
# already exists then be careful because you will overwrite it
fout = open('output.txt','w')
print fout

line1 = 'this here"s the wattle, \n'
fout.write(line1)

line2 = 'the emblem of our land. \n'
fout.write(line2)
fout.close()

s = '1 2\t 3 \n 4'
print s
print repr(s)
