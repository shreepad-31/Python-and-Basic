# Numbers: fractions(), decimal(), Complex number in form of 3+4j

# Set is treated as numbers in many cases
setone = {1,2,3,4}
# We can perfrom operations like intersection, union

# bool --> True and Flase, True == 1 and False == 0

import math

print(math.floor(-3.5))
# floor works as GIF

print(math.trunc(2.8))
# trunc takes you to the Integer closet to zero

print(math.ceil(14/4))
# Next nearest integer greater or equal

print(abs(10-100))
# Prints absolute value of given

from decimal import Decimal
# Import it when working with decimals

from fractions import Fraction
# similarly import it when working with fractions

import random

print(random.random())
# Give any random number

print(random.randint(1,10))
# Gives any random number between the range 1 to 10

ln = ['lemon', 'almond', 'ginger', 'mint']
print(random.choice(ln))
# chooses randomly from ln

# for Space separated Input:
x, y, z = map(int, input().split())
num = list(map(int, input().split()))