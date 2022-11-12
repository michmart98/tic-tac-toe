import os

### this is a method to clear the diplay of our console
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



