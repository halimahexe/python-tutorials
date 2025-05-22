def greet():
    """Greet player at start of game"""
    print("Welcome to Tic-Tac-Toe\n")
    print("Would you like to play?\n")
    print("Enter 'Y' to start a new game or 'N' to quit.\n")


def draw_board(squares):
    """Program used to draw tic tac toe board"""
    index = 1
    board = ""
    for key, value in squares.items():
        if index % 3 == 0:
            board += f"|{value}|\n"
        else:
            board += f"|{value}"
        index += 1
    print(board)


def check_turn(turn):
    """Check which player's turn it is and set the correct mark"""
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'


def check_input(input, squares):
    """Check for valid input"""
    # Check if the player gave a number 1-9
    if str.isdigit(input) and int(input) in squares:
        # Check if square is empty
        if not squares[int(input)] in {'X', 'O'}:
            # Valid input
            return True
    else:
        # Invalid input
        return False


def check_for_win(squares):
    """Check if player has won"""
    # Check for horizontal cases
    if squares[1] == squares[2] == squares[3] and squares[1] != ' ' \
            or squares[4] == squares[5] == squares[6] and squares[4] != ' ' \
            or squares[7] == squares[8] == squares[9] and squares[7] != ' ':
        return True
    # Check for vertical cases
    elif squares[1] == squares[4] == squares[7] and squares[1] != ' ' \
            or squares[2] == squares[5] == squares[8] and squares[2] != ' ' \
            or squares[3] == squares[6] == squares[9] and squares[3] != ' ':
        return True
    # Check for diagonal cases
    elif squares[1] == squares[5] == squares[9] and squares[1] != ' ' \
            or squares[3] == squares[5] == squares[7] and squares[3] != ' ':
        return True
    else:
        return False
