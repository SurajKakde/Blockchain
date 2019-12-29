# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
from random import random, randrange
from datetime import datetime


rand1 = random()
print(rand1)

rand2 = randrange(1, 10)
print(rand2)
# 2) Use the datetime library together with the random number to generate a random, unique value.

unique_value = str(rand1) + str(datetime.now())
print(unique_value)
