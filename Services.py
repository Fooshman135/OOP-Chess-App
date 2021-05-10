# Services

from Model import *
from View import *
import Globals



def letter_index_to_letter(letter_index):
    if 1 <= letter_index <= 8:
        return chr(97 + letter_index - 1)      # chr(97) produces the ASCII value "a"
    else:
        # Throw error
        raise Exception("This is an error!")



def square_indices_to_string(letter_index, number_index):
    return letter_index_to_letter(letter_index) + str(number_index)



def color_number_to_text(num):

    # Black = 0, White = 1

    if num == 0:
        text = "Black"
    elif num == 1:
        text = "White"
    else:
        # Throw error
        raise Exception("This is an error!")        

    return text



def produce_path_between_two_squares(square_one, square_two, board):
    """
    board: Container from which any square on the board can be retrieved from.
    square_one and square_two do not necessarily need to be members of board.
    """

    x1 = square_one.letter_index
    y1 = square_one.number_index
    x2 = square_two.letter_index
    y2 = square_two.number_index

    path = []

    if x1 == x2 and y1 == y2:
        # Squares are the same.
        pass
    elif x1 == x2:
        # Same column
        y = min(y1,y2) + 1
        while True:
            if y == max(y1,y2):
                # Reached the end of the path.
                break
            else:
                path.append(board.dict_of_64_squares[square_indices_to_string(x1,y)])
                y += 1
    elif y1 == y2:
        # Same row
        x = min(x1,x2) + 1
        while True:
            if x == max(x1,x2):
                # Reached the end of the path.
                break
            else:
                path.append(board.dict_of_64_squares[square_indices_to_string(x,y1)])
                x += 1
    elif abs(x1 - x2) == abs(y1 - y2):
        # Same diagonal
        if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
            # Diagonal runs bottom-left to top-right (or vice versa)
            x = min(x1, x2) + 1
            y = min(y1, y2) + 1
            while True:
                if x == max(x1,x2):
                    # Reached the end of the path.
                    break
                else:
                    path.append(board.dict_of_64_squares[square_indices_to_string(x,y)])
                    x += 1
                    y += 1
        elif (x1 < x2 and y1 > y2) or (x1 > x2 and y1 < y2):
            # Diagonal runs bottom-right to top-left (or vice versa)
            x = min(x1, x2) + 1
            y = max(y1, y2) - 1
            while True:
                if x == max(x1,x2):
                    # Reached the end of the path.
                    break
                else:
                    path.append(board.dict_of_64_squares[square_indices_to_string(x,y)])
                    x += 1
                    y -= 1
    else:
        # No straight path between squares.
        pass

    return path



def set_global_white_on_bottom(color_on_bottom):

    if color_on_bottom == 1:
        Globals.WHITE_ON_BOTTOM = True
    elif color_on_bottom == 0:
        Globals.WHITE_ON_BOTTOM = False
    else:
        # Throw error
        raise Exception("This is an error!")



def get_and_validate_user_input(game, is_source):

    while True:

        user_input = request_user_input_for_square(is_source)

        if is_source is False and user_input is None:
            # User wants to cancel choosing destination square.
            return user_input


        # INPUT VALIDATION TYPE 2: Confirm that the source input references a square that contains one of the player's pieces.
        # INPUT VALIDATION TYPE 3: Confirm that the destination input references a square that does not contain the current player’s piece.
        if game.current_board.dict_of_64_squares[user_input].contains_specified_players_piece(game.whose_turn) is not is_source:
            if is_source:
                display_error_message(2)
            else:
                display_error_message(3)
            continue

        return game.current_board.dict_of_64_squares[user_input]

