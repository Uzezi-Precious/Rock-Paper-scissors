import random

choice = ["R", "P", "S"]

print("WELCOME TO ROCK, PAPER SCISSORS!!!\nYOU ARE PLAYING WITH THE COMPUTER")
print("To play, \nR- Rock \nP - Paper \nS - Scissors")

computer_choice = random.choice(choice).upper()


while True:
    player = input("Choose R, P or S: ").upper()
    print()
    print("Player (" + player + ") : CPU (" + computer_choice + ")")
    
    if player == computer_choice:
        print("its a tie")
    elif player == "R" and computer_choice == "P":
        print("CPU wins")
        break
    elif player == "R" and computer_choice == "S":
        print("Player wins!")
        break
    elif player == "P" and computer_choice == "R":
        print("Player wins")
        break
    elif player == "P" and computer_choice == "S":
        print("CPU wins")
        break
    elif player == "S" and computer_choice == "R":
        print("Player wins")
        break
    elif player == "S" and computer_choice == "P":
        print("Player wins")
        break
    else:
        print("Wrong input! Try again.")
