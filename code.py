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

### Get Player Input
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


