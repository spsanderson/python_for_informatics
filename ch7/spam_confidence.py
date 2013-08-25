# Open a file and extract from it the spam confidence
fname = raw_input('Enter a file to open:')
try:
    fhand = open(fname)
except:
    print 'The file could not opened or could not be found'
    exit()

