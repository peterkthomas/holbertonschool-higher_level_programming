#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if n < 0:
    n *= -1
n = n % 10
if number < 0:
    n *= -1

if n > 5:
    message = 'is greater than 5'
elif n == 0:
    message = 'is 0'
else:
    message = 'is less than 6 and not 0'
print("Last digit of %d is %d and %s" % (number,n,message))
