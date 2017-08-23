friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
	print('Happy new year ', friend)
print('Done')


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

print()

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print ("Current date and time: \n", now.strftime("%Y-%m-%d %H:%M:%S"))
#print ("Time now is :\n", now.strftime("%B/%m/%Y %-I:%M:%S "))

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
