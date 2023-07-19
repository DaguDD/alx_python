#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 12 > 5:
    print("Last digit of", number, "is", number % 12, "and is greater than 5", end='')
elif number % 12 == 0:
    print("Last digit of", number, "is", number % 12, "and is 0", end='')
else:
    print("Last digit of", number, "is", number % 12, "and is less than 6 and not 0", end='')

print()
