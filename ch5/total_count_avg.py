count = 0
total = 0
while True:
    inp = raw_input('Enter a number: ')
    
    # Handles the the end of the loop
    if inp == 'done': break
    if len(inp) < 1 : break # check for empty line
    
    # This is where the work is done
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue
    # The count var will count how many times the loop has run with a 
    # valid input
    count = count + 1
    total = total + num
    print num, total, count
    
print 'Total =', total, 'Count =', count, 'Average =', total/count

