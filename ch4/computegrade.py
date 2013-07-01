# Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range print an error. If the score is between
# 0.0 and 1.0, print a grade using the following:
# >= 0.9 A; 80 <= x < 90 B etc

def computegrade(score):
    if score > 1.0 or score < 0.0:
        print 'Please enter a number between 0.0 and 1.0'
    elif 1.0 >= score >= 0.9:
        print 'A'
    elif 0.8 <= score < 0.9:
        print 'B'
    elif 0.7 <= score < 0.8:
        print 'C'
    elif 0.6 <= score < 0.7:
        print 'D'
    else:
        print 'F'
    
try:
    inp = float(raw_input('Please enter a Score between 0.0 and 1.0 \n'))
    print 'You entered ' + str(inp)
except:
    print 'Please enter a number between 0.0 and 1.0'
    quit()

grade = computegrade(inp)
