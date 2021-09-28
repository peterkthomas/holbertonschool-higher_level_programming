#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = number * -1
    last_digit = number % 10
else:
    last_digit = number % 10
if number > 5:
    message = 'is greater than 5 and not 0'
elif number < 0:
    message = 'is less than 5 and not 0'
else:
    message = 'is 0'
print("Last digit of %d is %d and %s" % (number,last_digit,message))
