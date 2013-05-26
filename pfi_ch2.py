# exercises from python for informatics chapter 2
# more at http://www.py4inf.com

# Write a programe that uses raw_input to prompt a user for their name
# and then welcomes them
input = raw_input('Enter your name: \n')
print ''
print 'Hi ' + input + ' thanks for stopping by'

# ask for hours worked and pay per hour to compute total pay 
hours_worked = float(raw_input('Please enter the hours you worked: \n'))
print ''
rate_per_hr = float(raw_input('Please enter your hourly rate: \n'))
rate_round = round(rate_per_hr, 2)
print ''
print 'Thank you we will now compute your pay'
print ''
pay = hours_worked * rate_round
print input + ' your pay is: ' + str(pay)
print ''

# Exercise 2.4, print the value and type of the expression
width = 17
height = 12.0
# exercises
w_div_2 = width/2
print w_div_2
print type(w_div_2)

w_div_2dot0 = width/2.0
print w_div_2dot0
print type(w_div_2dot0)

h_div_3 = height/3
print h_div_3
print type(h_div_3)

add_n = 1 + 2 * 5
print add_n
print type(add_n)

# Ask user to give temp in degrees C and convert to degrees F
user_temp = float(raw_input('Please enter the temp in Celcius: \n'))
celcius_to_farenheit = (((user_temp * 9) / 5) + 32)
print 'The temp in degrees F is ' + str(celcius_to_farenheit)

