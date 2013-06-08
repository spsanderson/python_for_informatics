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
    
