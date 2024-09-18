# project 3
# Rock, Paper, Sicssor game


# To get random O/p from Computer
import random

# Welcome user
print("\nWelcome to Rock, Paper, Sicssor game!\n\nHere are some rules of game\n1. Rock VS Paper = Paper wins\n2. Paper VS Scissor = Sicssor\n3. Scissors VS Rock = Rock win\n4. If same choice then, Its a tie\n")

# Now assigning values
Rock = 1
Paper = 2
Scissor = 3

# Score 
score_counter_player = 0
score_counter_comp = 0

while True:
    print("\nLet's begin!\nRock = 1\nPaper = 2\nScissor = 3\n")
    choice = int(input("Choose a number : "))
    while choice < 1 or choice > 3:
        choice = int(input('Enter a number between 1-3\n'))

    if choice == 1:
        choice_n = "Rock"
    elif choice == 2:
        choice_n = "Paper"
    else:
        choice_n = "Scissor"

    print(f"You'r choice is {choice_n}\n")
    # computer choice
    print("Computer is choosing....")
    computer_choice = random.randint(1,3)
    
    if computer_choice == 1:
        computer_choice_n = "Rock"
    elif computer_choice == 2:
        computer_choice_n = "Paper"
    else:
        computer_choice_n = "Scissor"

    print(f"Computer choice is {computer_choice_n}\n")
    print(f"{choice_n} VS {computer_choice_n}\n")

    # Game Logic
    if choice_n == computer_choice_n:
        result = "Tie"
    elif (choice_n == "Rock" and computer_choice_n == "Paper") or (choice_n == "Paper" and computer_choice_n == "Rock"):
        result = "Paper"
    elif (choice_n == "Rock" and computer_choice_n == "Scissor") or (choice_n == "Scissor" and computer_choice_n == "Rock"):
        result = "Rock"
    elif (choice_n == "Paper" and computer_choice_n == "Scissor") or (choice_n == "Scissor" and computer_choice_n == "Paper"):
        result = "Scissor"

    if result == "Tie":
        print("<< It's a Tie >>")
    elif result == choice_n:
        print("<< You Won! >>")
    elif result == computer_choice_n:
        print("<< Computer Won! >>")

    # Score count
    if result == choice_n:
        score_counter_player += 1
        print(f"Score {score_counter_player} : {score_counter_comp}\n")
    elif result == computer_choice_n:
        score_counter_comp += 1
        print(f"Score {score_counter_player} : {score_counter_comp}\n")

    a = input("Want to play again? (Y/N)\n").lower()
    if a == "n":
        break
print("Thank You for playing")