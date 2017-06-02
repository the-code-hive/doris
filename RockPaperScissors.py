#define Player 1 + 2
#Player 1=Human / input
#player 2=computer / choose random word from list
#say who wins
#Player1=human
#Player2=computer

import random

print ("You are playing Rock, Paper, Scissors!")

human=input("Please spell correctly and choose either Rock, Paper, or Scissors. ")
computer=random.choice(["rock", "paper", "scissors"])
print (computer)

if human.lower() == computer:
    print ("It's a tie")
elif human.lower() == "rock" and computer == "scissors":
    print ("You won!")
elif human.lower() == "paper" and computer == "rock":
    print ("You won!")
elif human.lower() == "scissors" and computer == "paper":
    print ("You won!")
else:
    print ("You lost!")
