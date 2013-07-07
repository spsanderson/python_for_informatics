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
    if largest is None or num > largest:
        largest = num
        #print 'Loop:', i, largest <-- used for testing
    print 'Largest',largest
    # Gets smallest number
    if smallest is None or num < smallest:
        smallest = num
        #print 'Loop:', i, smallest <-- used for testing
    print 'Smallest', smallest
    
print 'Count:', count, 'Largest:', largest, 'Smallest:', smallest
