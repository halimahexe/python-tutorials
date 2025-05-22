import os
from helpers import check_for_win, check_input, check_turn, draw_board, greet

# Declare variables
squares = {1: ' ', 2: ' ', 3: ' ', 4: ' ',
           5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
game_is_running, complete = False, False
player = 1
turn = 0
prev_turn = -1


def reset():
    """Reset game back to defaults"""
    global squares, player, turn, prev_turn

    squares = {1: ' ', 2: ' ', 3: ' ', 4: ' ',
               5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    player = 1
    turn = 0
    prev_turn = -1


# If game isn't running, greet player and ask if they want to play
if not game_is_running:
    greet()
    choice = input()
    if choice == 'Y':
        print()
        game_is_running = True
    elif choice == 'N':
        print('You have quit')

while game_is_running:
    # Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(squares)

    # Let player know if input was invalid
    if (prev_turn == turn):
        print("Invalid square selected. Please select a number between 1 and 9")
    prev_turn = turn
    player = (turn % 2) + 1
    print()
    print(f"Player {player}'s turn. Please pick a square or press 'q' to quit.")

    # Get input from player
    choice = input()
    # Check if player wants to quit
    if choice == 'q':
        game_is_running = False
        print('Game ended. Thanks for playing.')
    # Check if the player gave a number 1-9
    elif check_input(choice, squares):
        # Valid input, update the board
        turn += 1
        squares[int(choice)] = check_turn(turn)

    # Check if player has won
    if check_for_win(squares):
        game_is_running, complete = False, True
    if turn > 8:
        game_is_running = False

    if not game_is_running:
        # Update the board one last time.
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(squares)
        # Declare if there's a winner
        if complete:
            print(
                f"Player {player} wins!")
        else:
            print("Draw!")

        # Ask if player wants to start a new game
        print("Thanks for playing.\n")
        print("Want to play again? Press 'Y' to continue.")
        choice = input()
        if choice == 'Y':
            # Reset everything to play again
            game_is_running, complete = True, False
            reset()
