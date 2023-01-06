# MODULE IMPORTS
# import math


first = 'John'
last = 'Smith'
# FORMATTED STRING W/ INTERPOLATION
message = f'{first} [{last}] is a coder'
# print(message)


x = 2.9
# print(round(x))
# print(abs(-2.9))
# print(math.ceil(2.9))
# print(math.floor(2.9))
# look up python math module to see documentation for all functions available


# guessing game
secret_number = 9
number_guesses = 0
while number_guesses < 3:
    guess = int(input("Guess: "))
    number_guesses += 1
    if guess == 9:
        print("You Win!")
        break
else:   # executes if a break didn't terminate the loop
    print("Sorry, you lost")










