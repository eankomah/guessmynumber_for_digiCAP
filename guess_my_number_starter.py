"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
# use code below  to generate a random integer between 30 and 50 for example
# print(random.randint(30, 50)10)

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

number = random.randint(1,99) #Declare random guess as number
print(f"I am tinking of a number between 1 and 99.")
myNumber = int(input("Enter your Guess: ")) #ask user to input his guessed number as myNumber

while myNumber != number: #terminate program if Guessed number is true
    if myNumber < number:  #Check if Guessed number is too low
        print(f"Your Guess is too low.")
        myNumber = int(input("Enter a new Guess: ")) #Ask user to guess again
    elif myNumber > number:#Check if Guessed number is too high 
        print(f"Your Guess is too high.")
        myNumber = int(input("Enter a new Guess: "))#Ask user to guess again
else:
    print(f"Congrats! The number was: {number}") #end program if Guessed number if True