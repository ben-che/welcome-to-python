def main():
    # Your code goes below: Be careful, as indentation is important in Python!

    # Sample Question:
    # Print the result of 10 plus 10:
    # Sample Answer:
    print(10 + 10)

    #######################
    # Questions start here:

    # 1. Use Python's math operators to convert 10 hours into seconds:

    # 2. Use Python's math operators to convert 60 seconds into hours:

    # 3. Assign the answers from the previous two questions to two separate variables. Add them together and save the sum in a new variable called total. Print this variable.
    
    # Questions end here
    #######################

# Don't modify the function call below:
main()



def answers():
    # 1.
    print(10*60*60)
    # 2.
    print(60/60./60.)
    # 3.
    hoursToSeconds = 10*60*60
    secondsToHours = 60/60./60.
    total = hoursToSeconds + secondsToHours
    print(total)

answers()