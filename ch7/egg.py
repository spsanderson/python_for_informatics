fname = raw_input('Enter a file name: ')
if fname == 'na na boo boo':
    print 'NA NA BOO BOO TO YOU TOO - YOU GOT PUNKED'
    exit()
    
try:
    fhand = open(fname)
except:
    print 'Sorry file could not be opened'
    exit()
count = 0;
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print 'There are',count,'subject lines in',fname
    
