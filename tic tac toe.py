#Cody Dzierzon
#12/10/18
#tic-tac-toe against a computer

#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#functions
def display_instructions():
    print("""Welcome to TIC TAC TOE
          In in TIC TAC TOE you will be competing against a computer to get
          three in a row


              0 | 1 | 2
              ---------
              3 | 4 | 5
              ---------
              6 | 7 | 8

              """)

def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y","n"):
          response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
            else:
                response = input(question)
        else:
            print("you must enter a number")
            response = input(question)
    return int(response)

x = ask_number("enter a number between 1 and 10",1,11)
print(x)











































