import math, random

################################################################################################################################################

def atmLogic(withdrawAmount):
    currentBalance = 100
    if (withdrawAmount > currentBalance):
        print("Error, you're too broke")
    elif (withdrawAmount <= currentBalance) :
        print("Success!")

atmLogic(100)
atmLogic(200)
atmLogic(50)

################################################################################################################################################

def atmOperations(action, amount):
    currentBalance = 100
    if (action == "withdraw" and amount <= currentBalance):
        print("Success, new balance is $" + str(currentBalance - amount) )
    elif (action == "withdraw" and amount > currentBalance):
        print("Failure")
    elif (action == "deposit"):
        print ("Success, new balance is $" + str(currentBalance + amount) )

atmOperations("withdraw", 100)
atmOperations("withdraw", 10)
atmOperations("withdraw", 150)
atmOperations("deposit", 100)

################################################################################################################################################

def rockPaperScissors(userInput, computerInput):
    print("Computer plays: " + computerInput)

    # Sample solution code:
    # cases of a draw
    if (computerInput == userInput):
        print("Draw!")
    elif ((computerInput == "rock" and userInput == "paper") or (computerInput == "paper" and userInput == "scissors") or (computerInput == "scissors" and userInput == "rock")):
        print("You win!")
    elif ((computerInput == "rock" and userInput == "scissors") or (computerInput == "paper" and userInput == "rock") or (computerInput == "scissors" and userInput == "paper")):
        print("You lose!")
    else:
        print("Invalid Input")
    return

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
rockPaperScissors("paper", computerPlays())
rockPaperScissors("scissors", computerPlays())