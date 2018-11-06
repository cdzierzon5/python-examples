#guess my number game
#cody and nick
#11/2/2018


import random
global attempts
global maxTries
global intRange
global gNumber
attempts = 0
maxTries = 5
intRange = "1-100"
gNumber = random.randrange(0, 100)


def menu():
    while True:
        print("This is a guess my number game.")
        start = input("Would you like to play? [play, credits, or quit] ")
        if start.lower() == "play":
            custom = input("Do you want to create your own parameters for the game? y/n ")
            if custom.lower() == "y":
                return options()
            if custom.lower == "n":
                return play()
        if start.lower() == "credits":
                return credits()
        if start.lower() == "quit":
            input("Press enter to quit")
            exit()
        else:
            print("Invalid Option")

    


def play():
    guess_1 = input("What is your guess? ")
    if guess_1.digit():
        if guess_1 == gNumber:
            print("You WON!")
            return menu()
        if guess_1 <= gNumber:
            print("incorrect")
            print("guess higher")
            attempts += 1
        if guess_1 >= gNumber:
            print("incorrect")
            print("guess lower")
            attemts += 1
    
    else:
        print("that is not a valid answer")
        return play()
    

def options():
    print("Max Tries is",maxTries+".")
    print("Range is",intRange+".")
    yn = input("Do you want to change max tries? [y/n]: ")
    if yn.lower() == "y":
        maxTries = input("Enter new Max tries: ")
    elif yn.lower() == "n":

        yn = input("Do you want to change range? [y/n]: ")
        if yn.lower() == "y":
            tempRange = input("’1-100’ or ‘1-200’ or ‘1-300’")
            if tempRange == "1-100":
                intRange = "1-100"
                print("range changed to 1-100")
            
            elif tempRange == "1-200":
                intRange = "1-200"
                print("range changed to 1-200")
            
            elif tempRange == "1-300":
                intRange = "1-300"
                print("range changed to 1-300")
            
            else:
                print("I don’t know what you mean")
        else:
            print("i dont know what that means")


def credits():
    print("This game was created on 11/2/2018 by Nick and Cody")
    cEnd = input("would you like to return to the menu?[y/n]")
    if cEnd.lower() == "y":
        return menu()
    else:
        print("too bad")
        return menu()

menu()
