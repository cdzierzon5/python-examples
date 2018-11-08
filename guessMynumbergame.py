#guess my number game
#cody and nick
#11/2/2018

import random
<<<<<<< HEAD

=======
global attempts
global maxTries
global intRange
global gNumber
>>>>>>> 94edbb3dea9dabffc84add99ae14c5baaf5dfa00
attempts = 0
maxTries = 5
intRange = "1-100"
gNumber = random.randrange(0, 100)

def menu():
    #main menu
    while True:
        print("This is a guess my number game.")
        start = input("Would you like to play? [play, credits, or quit] ")
        if start.lower() == "play":
            custom = input("Do you want to create your own parameters for the game? y/n ")
            if custom.lower() == "y":
                return options()
            if custom.lower() == "n":
                return play()
        if start.lower() == "credits":
                return credits()
        if start.lower() == "quit":
            input("Press enter to quit")
            exit()
        else:
            print("Invalid Option")

<<<<<<< HEAD
#play allows for the player to guess a number
def play():
    global attempts
    global maxTries
    global gNumber
    while True:
        if attempts >= int(maxTries):
            print("You ran out of attempts!")
            maxTries = 5
            gNumber = random.randrange(0, 100)
            return menu()
        guess_1 = int(input("What is your guess? "))
        if guess_1:
            if guess_1 == gNumber:
                print("You WON!")
                attempts = 0
                return menu()
            else:
                if guess_1 < gNumber:
                    print("incorrect")
                    print("guess higher")
                    attempts += 1
                    
                elif guess_1 > gNumber:
                    print("incorrect")
                    print("guess lower")
                    attempts += 1
                    
        
    else:
        print("that is not a valid answer")
        return play()

#options allows for changing in the attepts and range
=======
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
    
>>>>>>> 94edbb3dea9dabffc84add99ae14c5baaf5dfa00
def options():
    global maxTries
    global intRange
    global gNumber
    global attempts
    print("Max Tries is",str(maxTries)+".")
    print("Range is",str(intRange)+".")
    yn = input("Do you want to change max tries? [y/n]: ")
    if yn.lower() == "y":
        newmaxTries = input("Enter new Max tries: ")
        maxTries = newmaxTries
        print("maxtries: ",maxTries)
        #attempts = newmaxTries

<<<<<<< HEAD
        
    if yn.lower() == "n":
        print("you said no")
    yn2 = input("Do you want to change range? [y/n]: ")
    if yn2.lower() == "y":
        tempRange = input("’1-100’ or ‘1-200’ or ‘1-300’")
        if tempRange == "1-100":
            intRange = "1-100"
            gNumber = random.randrange(0, 100)
            print("range changed to 1-100")
            return play()
        
        elif tempRange == "1-200":
            intRange = "1-200"
            gNumber = random.randrange(0, 200)
            print("range changed to 1-200")
            return play()
        
        elif tempRange == "1-300":
            intRange = "1-300"
            gNumber = random.randrange(0, 300)
            print("range changed to 1-300")
            return play()
        if tempRange.lower() == "n":
            print("you didn't change the range")
            return play
        else:
            print("I don’t know what you mean")
    else:
        print("i dont know what that means")

#credits showing who made the game and when
=======
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

>>>>>>> 94edbb3dea9dabffc84add99ae14c5baaf5dfa00
def credits():
    print("This game was created on 11/2/2018 by Nick and Cody")
    cEnd = input("would you like to return to the menu?[y/n]")
    if cEnd.lower() == "y":
        return menu()
    else:
        print("too bad")
        return menu()

menu()
