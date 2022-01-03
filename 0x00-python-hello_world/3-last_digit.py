#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
pos = abs(number) % 10
neg = -pos
print("Last digit of", number, "is", pos if number >= 0 else neg, end=" ")
if pos == 0:
        print("and is 0")
elif pos > 5 and number > 0:
        print("and is greater than 5")
else:
        print("and is less than 6 and not 0")
