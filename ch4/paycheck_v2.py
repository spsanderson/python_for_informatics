# Define a function called computepay
def computepay(r, h):
    print "In computepay function", h, r
    if hours_worked <= 40:
        p = h * r
    else:
        p = r * 40 + (r * 1.5 * (h - 40))
    print "Finished with computepay", p
    return p

# ask for hours worked and pay per hour to compute total pay 
try:
    hours_worked = float(raw_input('Please enter the hours you worked: \n'))
    print ''
except:
    print 'Please enter hours as a number'
    quit()
try:
    rate_per_hr = float(raw_input('Please enter your hourly rate: \n'))
    rate_round = round(rate_per_hr, 2)
    print ''
except:
    print 'Please enter rate per hour as a number'
    quit()

if hours_worked <= 40:
    pay = hours_worked * rate_round
else:
    pay = rate_round * 40 + (rate_round * 1.5 * (hours_worked - 40))
print 'Your pay is ' + str(pay)

print "The rate and hours in try/except code", rate_per_hr, hours_worked
pay = computepay(hours_worked, rate_per_hr)
print "We are back", pay

