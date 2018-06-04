import math

def answers():
    # 1.
    print(10*60*60) # prints 36000 to console
    # 2.
    print(60/60./60.) # prints 0.01666... to console
    # 3.
    hoursToSeconds = 10*60*60
    secondsToHours = 60/60./60.
    total = hoursToSeconds + secondsToHours
    print(total) # prints 36000.016666... to console
    # 4.
    stringy = "1000"
    # 5.
    print(stringy+total) # we end up with an error - we can't add strings with decimal numbers. be sure to read any future error messages you get!

answers()