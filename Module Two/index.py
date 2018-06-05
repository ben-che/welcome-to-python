import math, random
# Create a rock paper scissors game that takes in user input and computer input and prints whether the user wins or loses:
def rockPaperScissors(userInput, computerInput):
    # Here, we run the computerPlays function, which will randomly generate "rock" "paper", or "scissors"
    print("Computer plays: " + computerInput)
    print("User plays:" + userInput)

    # Write your conditional flow below:
        # Hint: Think about the win / lose / tie conditions

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

# Call 
rockPaperScissors("rock", computerPlays())
rockPaperScissors("paper", computerPlays())
rockPaperScissors("scissors", computerPlays())