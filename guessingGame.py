import random

numberToGuess = random.randint(1,100)
attempts = 0

while attempts<10:
    try:
        myGuess = input("Guess an integer between 1 and 100: ")
        val = int(myGuess)
    except ValueError:
        print("That is not a number smfh bruh")
    else:
        if val>100 or val<1:
            print("Reading isn't that hard lol... you're not even in bounds")
        if val == numberToGuess:
            print("you got it!")
            break;
        elif val>numberToGuess:
            print("too high!")
            attempts +=1
        elif val<numberToGuess:
            print("too low")
            attempts +=1
        else:
            raise AssertionError("What is this lol")

if attempts==10:
    print("wow you're bad at this")
    print ("the answer was", numberToGuess)