count = 0
largest = None
smallest = None

while True:
    inp = raw_input('Please enter a number: ')
    # Kills the program
    if inp == 'done' : break
    if len(inp) < 1 : break
    
    # Gets the work done
    try:
        num = float(inp)
    except:
        print 'Invalid input, please enter a number'
        continue
    # The numbers for count, largest and smallest
    count = count + 1
    # Gets largest number
    for i in inp:
        if largest is None or i > largest:
            largest = i
        #print 'Loop:', i, largest <-- used for testing
    print 'Largest',largest
    # Gets smallest number
    for i in inp:
        if smallest is None or i < smallest:
            smallest = i
        #print 'Loop:', i, smallest <-- used for testing
    print 'Smallest', smallest
    
print 'Count:', count, 'Largest:', largest, 'Smallest:', smallest
