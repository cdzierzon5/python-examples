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
          In this game of TIC TAC TOE you will be competing against a computer
          to get three in a row


              0 | 1 | 2
              ---------
              3 | 4 | 5
              ---------
              6 | 7 | 8

              """)
##############################################################################
def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y","n"):
          response = input(question).lower()
    return response
##############################################################################
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
##############################################################################
def pieces():
    go_first = ask_yes_no("Would you like to go first? y/n ")
    if go_first == "y":
        print("\nThen take the first move. You will need it.")
        human = X
        computer = O
    else:
        print("\nYou think you can beat me!? Your bravery will be your undoing... I will go first")
    return computer, human
##############################################################################
def new_board():
    board = []
    for squares in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
##############################################################################
def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8])
##############################################################################
def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
        else:
            continue
    return moves
##############################################################################
def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
          winner = board[row[0]]
          return winner

    if EMPTY not in board:
        return TIE

    return None
##############################################################################    
def human_move(board):
    move = None
    legal = legal_moves(board)
    while move not in legal:
        move = ask_number("Where would you like to go? ",0,9)
        if move not in legal:
            print("WOW, you think you can go there...trying to cheat to win...foolish human")
    return move
##############################################################################
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X
##############################################################################
def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print(the_winner,"won!\n")
    else:
        print("It is a tie!\n")

    if the_winner == computer:
        print("As I have predicted, I am superior!")

    elif the_winner == human:
        print("You have bested me this time...BUT NEVER AGAIN")

    elif the_winner == TIE:
        print("You got lucky this time...and managed to TIE me")
##############################################################################
def computer_move(board, computer, human):
    #make a copy of this to work with since function will be changing list
    board = board[:]
    #the best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I will play in square number", end=" ")

    #if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #done checking this
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        #done checking this
        board[move] = EMPTY

    #since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
##############################################################################
def main():
    display_instructions()
    computer, human = pieces()
    board = new_board()
    turn = X
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        turn = next_turn(turn)
        display_board(board)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
    
main()
input("press enter to exit")

































