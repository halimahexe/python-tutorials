from helpers import draw_board, greet, check_turn, player_input
import os

squares = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}
player = 1
mark = 'X'

game_is_running = False
turn = 1

# Check if game is running
# If it's not running, ask if the player wants to start a new game
# To start a new game, draw the board
# Assign a mark to the player and ask them to select a square
# Check whether the player has won the game, if not play moves to
# next player

if not game_is_running:
    greet()
    choice = input()
    if choice == 'Y':
        print()
        game_is_running = True
    elif choice == 'N':
        print('You have quit')

while game_is_running:
    if turn == 10:
        print("End of game!")
        game_is_running = False
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(squares)
        print(f"It is Player {player}'s turn.")
        print("Enter the number of the square you want to mark")
        choice = input()
        if choice == 'q':
            print('Game ended. Thanks for playing')
            game_is_running = False
        else:
            player_input(squares, choice, mark)
            turn += 1
            player = (turn % 2) + 1
            mark = check_turn(turn)
            print(turn)
