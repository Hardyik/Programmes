#number guesser 

# importing random libraries
import random

# welcome user
print("Hello! Welcome to Number Guessing Game,\nYou got 7 chances to win the game,\nGuess a number between 1 to 50,\nLets begin!")

# importing a random number out of 50
random_number = random.randrange(50)

#Chance to guess the number
chance = 7

# Guessing Start from 0 
starting_guess = 0

#Block of code
while chance > starting_guess:
    starting_guess += 1
    guess = int(input('Guess the number: '))
    
    #If guessed number is right
    if guess == random_number:
        print(f"Hurray!! The number is {random_number} You guessed it right!\nIn your {starting_guess} attempt!")
        break

    #Out of chances
    elif starting_guess >= chance and guess != random_number:
        print(f"Sorry...., but the number is {random_number} and you are out of chances\nBetter luck next time!")

    # if guess is smaller
    elif guess < random_number:
        print("Worng guess!,\nYour number is smaller.")

    # if guess is greater 
    elif guess > random_number:
        print("Wrong guess!,\nYour number is greater.")