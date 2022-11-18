from functions import display_board, player_input, place_marker, win_check, choose_first, full_board_check, player_choice, replay

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print('Randomly we will select which one of you plays first')
    print(turn + ' will go first.')
    
    play_game = ""
    while play_game.lower != "yes" or play_game.lower != "no":
        play_game = input('Are you ready to play? Enter Yes or No. ')
        if play_game.lower() == 'yes':
            game_on = True
            break
        elif play_game.lower() == 'no':
            game_on = False
            break
        else:
            print('Please input a valid option')


    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            print("Player1")
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            print("Player2")
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break