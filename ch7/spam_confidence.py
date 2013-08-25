# Open a file and extract from it the spam confidence
fname = raw_input('Enter a file to open: ')
try:
    fhand = open(fname)
except:
    print 'The file could not opened or could not be found'
    exit()

count = 0;
spam_level = 0;

for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        spam_level = spam_level + float(line[-6:])
        
print 'Total messages counted:',count
print 'Total spam_level:',spam_level
print 'The average spam confidence level is',spam_level/count
    
