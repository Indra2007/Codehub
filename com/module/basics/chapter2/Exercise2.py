"""
Exercise 2: Write a program that uses input to prompt a user for their name and
then welcomes them.
Enter your name: Chuck
Hello Chuck

"""

name = input('Enter your name: ')
print('Hello ', name, '!')

"""
Exercise 3: Write a program to prompt the user for hours and rate per hour to
compute gross pay.
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
"""

hour = int(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

"""
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
hourly rate for hours worked above 40 hours.
"""

if hour > 40:
  extra_time = float(hour) - 40
else:
  extra_time = 0

extra_pay = 0.5 * float(rate) * extra_time

pay = float(hour) * float(rate) + extra_pay
print('Pay: ',pay)

"""
Exercise 5: Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit, and print out the converted temperature.
"""

print('Celsius to Fahrenheit Conversion')
celsius = float(input('Celsius: '))
fahrenheit = (celsius * 9 / 5) + 32

print ('Fahrenheit: ' + str(fahrenheit))