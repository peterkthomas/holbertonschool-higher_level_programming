#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number
if last_digit < 0:
    last_digit *= -1
last_digit = last_digit % 10
if number > 5:
    message = 'is greater than 5'
elif number < 0:
    message = 'is less than 5'
else:
    message = 'is 0'
print("Last digit of %d is %d and %s" % (number,last_digit,message))
