import math, random
################################################################################################################################################

# Create a simple ATM system that either prints "Success" if the user has enough money for a withdraw, or "Error" if they do not have
#   enough funds
# Sample Tests:
#   atmLogic(100) => "Success"
#   atmLogic(10) => "Success"
#   atmLogic(1000) => "Error"

def atmLogic(withdrawAmount):
    currentBalance = 100
    # Define function below:

################################################################################################################################################

# Let's add more functionality to our original function - in addition to an amount, we're going to add a string that tells the atm
#   if we're depositing or withdrawing money. The function should print success or failure, as well as an updated amount to the console
#   in the case of a success
# Sample Test:
#   atmOperations("withdraw", 100) => "Success - your new balance is $0"
#   atmOperations("withdraw", 10) => "Success - your new balance is $90"
#   atmOperations("withdraw", 150) => "Error, not enough money"
#   atmOperations("deposit", 100) => "Success - your new balance is $200"

def atmOperations(action, amount):
    currentBalance = 100

################################################################################################################################################

# Create a rock paper scissors game that takes in user input and computer input and prints whether the user wins, draws or loses:
# Sample Tests:
#   rockPaperScissors("rock","paper") => prints "You lose!"
#   rockPaperScissors("paper","paper") => prints "Draw!"
#   rockPaperScissors("scissors","paper") => prints "You win!"

#   bonus: a statement that handles invalid input
#   #   rockPaperScissors("herp","derp") => prints "Invalid input"

def rockPaperScissors(userInput, computerInput):
    # Here, we run the computerPlays function, which will randomly generate "rock" "paper", or "scissors"
    print("Computer plays: " + computerInput)
    print("User plays:" + userInput)

    # Write your conditional flow below:
        # Hint: Think about the win / lose / tie conditions and what gets printed


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

# Tests: 
rockPaperScissors("rock", computerPlays())
rockPaperScissors("paper", computerPlays())
rockPaperScissors("scissors", computerPlays())

################################################################################################################################################