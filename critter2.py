#Cody Dzierzon
#1/22/19

import time
import random

class Critter(object):

    """A virtual pet"""
    def __init__(self,name):
        print("a critter has been born!")
        self.name = name
        self.__hunger = hunger
        self.__boredom = boredom

    def __pass_time(self):
        self.__hunger += 1
        self.__boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            mood = "HAPPY"
        elif 5 <= unhappiness <= 10:
            mood = "okay"
        elif 11 <= unhappiness <= 15:
            mood = "frustrated"
        else:
            mood = "MAD"
        return mood

    def talk(self):
        print("\nHi, I'm", self.name)
        print("\nI am in a",self.mood)
        self.__pass_time()

    def eat(self, food):
        print("how many slices of pizza do you want to feed ",self.name+"?")
        food = int(input("(1-8 slices) "))
        if 1<= food <=3:
            print("are you trying to starve you critter!?\nYou fed", self.name,"but it is still a little hungry")
            self.hunger -= food
            if self.hunger < 0:
                self.hunger = 0
            self.__pass_time()
        elif 3< food <= 6:
            print("your critter is well fed")
            self.hunger -= food
            if self.hunger < 0:
                self.hunger = 0
            self.__pass_time()
        elif 6< food <= 8:
            print("your citter will be full for a while")
            self.hunger -= food
            if self.hunger < 0:
                self.hunger = 0
            self.__pass_time()
        else:
            print("that is not a valid option")

    def play(self, fun):
        print("your critter wants to play with you. How long do you want to play with", self.name+"?")
        fun = int(input("1min - 60 min"))
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
        if 1<= fun <20:
            print("you should play with your critter longer")
            self.boredom -= fun
            if self.boredom < 0:
                self.boredom = 0
            self.__pass_time()

        elif 20<= fun < 40:
            print("your critter is in a better mood now")
            self.boredom -= fun
            if self.boredom < 0:
                self.boredom = 0
            self.__pass_time()

        elif 40<= fun <= 60:
            print(self.name,"had a lot of fun and is no longer mad at you")
            self.boredom -= fun
            if self.boredom < 0:
                self.boredom = 0
            self.__pass_time()

        else:
            print("that is not a valid option")

    def main():
        crit_name = input("what would you like to set you critters name as? ")
        crit = crit_name
        choice = None
        while choice != "0":
            print("How would you like to interact with your critter?\n 0-quit \n 1-have", crit,"talk\n 2-feed", crit,"\n 3-play with", crit)
            choice = input("0,1,2,3: ")
            print(choice)
            # exit
            if choice == "0":
                print("good bye")
                exit()
            # listen to your critter
            elif choice == "1":
                crit.talk()
            # feed your critter
            elif choice == "2":
                crit.eat()
            # play with your critter
            elif choice == "3":
                crit.play()
            # some unknown choice
            else:
                print("that is not a good choice")
    main()
    ("\n\nPress enter to exit")




