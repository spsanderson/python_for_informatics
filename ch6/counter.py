# will count the the occurances of 'letter' in 'string' and print out
# the count of 'letter' in 'string'
def count(string, letter):
    count = 0
    for i in string:
        if i == letter:
            count = count + 1
    print count
