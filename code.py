import os

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

demo_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(demo_board)

### Get Player Inputm assign marker to each player
def player_input():
    marker = ''
    
    while marker != "X" and marker != "O":
        marker = input ('Player 1 please choose X or O as your move: ').upper()
        # .upper in order not to have an extra check for small x or o

        if marker == "X":
            return ('X','O')
        elif marker == "O":
            return ('O','X')
        else:
            print(f"{marker} is not a valid option. Please type X or O")
player1_marker, player2_marker = player_input()
print(f"The player 1 has marker {player1_marker}, The player 2 has marker {player2_marker}")

### Place marker in the board, according to user input
def place_marker(board, marker, position):
    while True:
        position = int(input("where to put the marker "))
        if position > 0 and position < 10:
            break
        else:
            print("Please provide a position in the range 0-9")
    board[position] = marker

place_marker(demo_board, player1_marker, 8)
display_board(demo_board)

### Victory Check, check all scenarios for victory, return true if the given mark won
def victory_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

victory_check(demo_board,'X')

### Space Check, check if a spot is empty
def space_check(board,position):
    return board[position] == " "

