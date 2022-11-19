import os
import random


### Clear the Console-Display function
def clear_disp():
    os.system('clear' if os.name=='nt' else 'clear')

### Build our display
def display_board(board):
    clear_disp()
    print(board[7] + "|" + board[8] + "|" + board[9])
    print('-----')
    print(board[4] + "|" + board[5] + "|" + board[6])
    print('-----')
    print(board[1] + "|" + board[2] + "|" + board[3])

### Get Player Input assign marker to each player
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1 will choose marker. Do you want to be X or O? ').upper()
        if marker == 'X':
            return ('X', 'O')
        elif marker == 'O':
            return ('O', 'X')
        else:
            print(f"{marker} is not a valid option. Please type X or O")



### Place marker in the board, according to user input
def place_marker(board, marker, position):
    board[position] = marker



### Win Check, check all scenarios for winning, return true if the given mark won
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal



### A function to random select who plays first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

### Space Check, check if a spot is empty, returns true if there is space left
def space_check(board, position):
    return board[position] == ' '

### Full Board, check if the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


### Next position for player's marker
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position

### Replay function
def replay():
    answer = ""
    while answer != True or answer != False:
        answer = input('Do you want to play again? Enter Yes or No: ').lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print('Please provide a valid answer')