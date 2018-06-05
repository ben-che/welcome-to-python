import math, random
# Create a rock paper scissors game that takes in user input and computer input and prints :
def rockPaperScissors(userInput, computerInput):
    # Here, we run the computerPlays function, which will randomly generate "rock" "paper", or "scissors"
    print("Computer plays: " + computerInput)

    # Write your conditional flow below:


# Code that generates computer input - you don't have to change anything here:
def computerPlays():
    rng = math.ceil(random.random() * 3)
    computerAnswer = ""
    if rng == 1:
        computerAnswer = "rock"
    elif rng == 2:
        computerAnswer = "paper"
    elif rng == 3:
        computerAnswer = "scissors"
    return computerAnswer


rockPaperScissors("rock", computerPlays())