#Importing Python 3 print function in order to use .format method on print statements
from __future__ import print_function

#Initializing global variables to default starting values
global ongoing
ongoing = True
global currentPlayer
currentPlayer = 1
global theBoard
theBoard = ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]']

#Function used to print the board out at the beginning and after every time board is marked
def display_board(board):
    position = 0
    for rows in range(0,3):
        for cols in range(0,3):
            print(board[position],end='')
            position +=1
        print('\n',end='')

#Function used to mark the board with either an 'X' or 'O' depending on whose turn it is
def mark_board(player, board):
    mark = ''
    if player == 1: mark = '[X]'
    if player == 2: mark = '[O]'
    chosenPosition = int(raw_input("Enter a position (1-9): "))
    while board[chosenPosition-1] != '[ ]':
        chosenPosition = int(raw_input("Position already occupied, enter another position (1-9): "))
    board[chosenPosition-1] = mark
    display_board(board)

#Function that runs through each win condition, if none are met it then checks if board is full
def check_condition(player, board):
    def check_horizontals(player, board):
        global ongoing
        if board[0] == board[1] == board[2] and board[0] != '[ ]':
            print('Player {x} wins from row 1 completion!'.format(x = player))
            ongoing = False
        if board[3] == board[4] == board[5] and board[3] != '[ ]':
            print('Player {x} wins from row 2 completion!'.format(x = player))
            ongoing = False
        if board[6] == board[7] == board[8] and board[6] != '[ ]':
            print('Player {x} wins from row 3 completion!'.format(x = player))
            ongoing = False
    def check_verticals(player, board):
        global ongoing
        if board[0] == board[3] == board[6] and board[0] != '[ ]':
            print('Player {x} wins from col 1 completion!'.format(x = player))
            ongoing = False
        if board[1] == board[4] == board[7] and board[1] != '[ ]':
            print('Player {x} wins from col 2 completion!'.format(x = player))
            ongoing = False
        if board[2] == board[5] == board[8] and board[2] != '[ ]':
            print('Player {x} wins from col 3 completion!'.format(x = player))
            ongoing = False
    def check_diagonals(player, board):
        global ongoing
        if board[0] == board[4] == board[8] and board[0] != '[ ]':
            print('Player {x} wins from primary diagonal completion!'.format(x = player))
            ongoing = False
        if board[2] == board[4] == board[6] and board[2] != '[ ]':
            print('Player {x} wins from secondary diagonal completion!'.format(x = player))
            ongoing = False
    def check_full(player, board):
        global currentPlayer
        global ongoing
        full = False
        if '[ ]' not in board and ongoing == True:
            full = True
        if full:
            print('Board is full and there is no winner.')
            ongoing = False
        else:
            if player == 1: currentPlayer = 2
            if player == 2: currentPlayer = 1
    check_horizontals(player, board)
    check_verticals(player, board)
    check_diagonals(player, board)
    check_full(player, board)

#Function that drives the game, continuously calling mark_board and check_condition functions
def play_game(board):
    global ongoing
    ongoing = True
    display_board(board)
    while ongoing == True:
        mark_board(currentPlayer, board)
        check_condition(currentPlayer, board)
    answer = raw_input("Do you want to play again? (Y/N):")
    if answer == "Y" or answer == "y":
        board = ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]']
        play_game(board)
    else:
        ongoing = False
 
#Calling driver function
while ongoing == True:
    play_game(theBoard)

    