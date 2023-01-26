
#import package random
import random

#input number and store
numInput = input("Type a number between 1 and 10 and press Enter... ")

#produce random integer between 1 and 10
randInteger = random.randint(1, 10)

#return 1 if numbers match, 0 if they do not
if numInput == randInteger:
  print(1)
else:
  print(0)

