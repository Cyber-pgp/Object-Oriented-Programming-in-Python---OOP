# Using random Module

# using random module
import random # we need to import the random module to us it

roll = random.randint(1,6) # this function will return the random number between 1 and 6

guess = int(input('Guess the dice roll:\n') # here we r converting the input to an int so we can compare guess to roll.

if guess == roll:
            print('Correct! They rolled a ' + str(roll))
            else:
            print('Wrong! They rolled a ' + str(roll))# here we converted the int to a string to concatenate it-
            
