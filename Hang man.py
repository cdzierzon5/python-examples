#hangman game
#cody dzierzon
#11-26-18
#The classic game of Hangman.

#imports
import random
import time

#constants
HANGMAN = (
"""
 _______
 |     |
 |     |
 |   
 | 
 |
 |
 |
 |
 |
------
""",
"""
 _______
 |     |
 |     |
 |     @
 |
 |
 |
 |
 |
 |
------
""",
"""
 _______
 |     |
 |     |
 |     @
 |     +
 |     +
 |
 |
 |
 |
------
""",
"""
 _______
 |     |
 |     |
 |     @
 |     +-\\
 |     +  \\
 |
 |
 |
 |
------
""",
"""
 _______
 |     |
 |     |
 |     @
 |   /-+-\\
 |  /  +  \\
 |
 |
 |
 |
------
""",
"""
 _______
 |     |
 |     |
 |     @
 |   /-+-\\
 |  /  +  \\
 |    |
 |    |
 |    
 |
------
""",
"""
 _______
 |     |
 |     |
 |     @
 |   /-+-\\
 |  /  +  \\
 |    | |
 |    | |
 |    
 |
------
""",
"""
 _______
 |     |
 |     |
 |     @
 |   /-+-\\
 |  /  +  \\
 |    | |
 |    | |
 |    - - 
 | DEEEED!!!
------
""")

max_wrong=len(HANGMAN)-1
words = ("PYTHON",
         "BOOLEAN",
         "INPUT",
         "LIST",
         "LENGTH",
         "WHILE",
         "EXPOSITORY",
         "FOR",
         "LOOP",
         "INTEGER",
         "VARIABLE",
         "INTERCHANGEABLENESS",
         "UNCHARACTERISTICALLY",
         "WANDERLUST",
         "COUNTERINTELLIGENCE",
         "INSTANTANEOUS",
         "CATTYWAMPUS",
         "GARDYLOO",
         "TARADIDDLE",
         "SNICKERSNEE",
         "WIDDERSHINS",
         "COLLYWOBBLES",
         "NONINTERVENTION",
         "INDISTINGUISHABILITY",
         "FLIBBERTIGIBBET",
         "GYPSYFY",
         "PANDICULATION",
         "TWYNDYLLYNGS",
         "RYTHM"<
         "INTERCONNECTION")
#the word to be guessed
word = random.choice(words)
#one dash for each letter in the word to be guessed
so_far = "-"*len(word)
#number of wrong guesses player has made
wrong = 0
#letters already guessed
used = []

print("WELCOME TO HANGMAN. good luck")

while wrong < max_wrong and so_far != word:

    print(HANGMAN[worng])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper


    while guess in used:
      print("You've already guessed the letter", guess)
      guess = input("Enter your guess: ")
      guess = guess.upper

    used.append(guess)

    if guess in word:
      print("\nYes!", guess, "is in the word!")

      #create new so_far to include guess
      new = ""
      for i in range(len(word)):
        if guess == word[i]:
            new += guess
        else:
            new += so_far[i]
      so_far = new
    else:
      print("\nSorry"< guess, "isn't in the word.")
      wrong += 1

if wrong  == max_wrong:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
    
else:
    print("\nYou guessed it!")
print("\nThe word was", word)

input("\n\nPress the enter key to exit.")









