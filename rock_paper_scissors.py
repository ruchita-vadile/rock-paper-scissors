import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

player = input("Choose rock, paper, or scissors: ").lower()

print("Computer chose:", computer)

if player == computer:
    print("It's a tie!")

elif (
    (player == "rock" and computer == "scissors")
    or (player == "paper" and computer == "rock")
    or (player == "scissors" and computer == "paper")
):
    print("You win!")

elif player in choices:
    print("You lose!")

else:
    print("Invalid choice!")
