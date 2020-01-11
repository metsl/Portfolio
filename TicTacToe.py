import random


def display_board(board):
    print('\n' * 100)
    print(f" {board[7]} | {board[8]} | {board[9]} \n---|---|---\n {board[4]} | {board[5]} | {board[6]} ")
    print(f"---|---|---\n {board[1]} | {board[2]} | {board[3]} ")


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[3] == marker and board[4] == marker and board[5] == marker) or
            (board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[3] == marker and board[6] == marker and board[9] == marker) or
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[3] == marker and board[5] == marker and board[7] == marker))


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Please enter a number from 1 to 9: '))
    return position


def replay():
    return input('Want to play again? (y/n): ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:

    turn = choose_first()
    print(turn + ' choosing first')
    player1_marker, player2_marker = player_input()
    board = [' '] * 10

    start_game = input("Are you ready to play? (yes/no)")

    if start_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            # Player 1 Turn
            display_board(board)  # displays board after each marker choise
            position = player_choice(board)
            place_marker(board, player1_marker, position)  # places a marker on the choosen position

            if win_check(board, player1_marker):  # checks if there is a win
                display_board(board)
                print("You won!")
                game_on = False

            else:
                if full_board_check(board):
                    display_board(board)
                    print("This is draw!")
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            display_board(board)  # displays board after each marker choice
            position = player_choice(board)
            place_marker(board, player2_marker, position)  # places a marker on the chosen position
            if win_check(board, player2_marker):  # checks if there is a win
                display_board(board)
                print("You won!")
                game_on = False

            else:
                if full_board_check(board):
                    display_board(board)
                    print("This is draw!")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
