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
 | DED!!!
------
""")

max_wrong=len(HANGMAN)-1
words = ("python",
         "boolean",
         )

for i in range(len(HANGMAN)):
    print(HANGMAN[i])
    time.sleep(5)
