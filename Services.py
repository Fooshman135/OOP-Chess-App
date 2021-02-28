# Services

from Model import *
from View import *



def letter_index_to_letter(letter_index):
    
    if letter_index == 1:
        x = "a"
    elif letter_index == 2:
        x = "b"
    elif letter_index == 3:
        x = "c"
    elif letter_index == 4:
        x = "d"
    elif letter_index == 5:
        x = "e"
    elif letter_index == 6:
        x = "f"
    elif letter_index == 7:
        x = "g"
    elif letter_index == 8:
        x = "h"
    else:
        # Throw error
        raise Exception("This is an error!")
    
    return x



def letter_to_letter_index(letter):
    
    if letter_index == "a":
        x = 1
    elif letter_index == "b":
        x = 2
    elif letter_index == "c":
        x = 3
    elif letter_index == "d":
        x = 4
    elif letter_index == "e":
        x = 5
    elif letter_index == "f":
        x = 6
    elif letter_index == "g":
        x = 7
    elif letter_index == "h":
        x = 8
    else:
        # Throw error
        raise Exception("This is an error!")
    
    return x




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



def get_square_from_indexes(array_of_squares,letter_index_here, number_index_here):

    # TODO (IS THIS NEEDED ANYMORE NOW THAT WE USE DICTIONARIES INSTEAD OF LISTS?)
    
    x = None

    for i in range(len(array_of_squares)):
        if (array_of_squares[i].letter_index == letter_index_here and array_of_squares[i].number_index == number_index_here):
            x = array_of_squares[i]
            break

    if x is None:
        # Throw error
        raise Exception("This is an error!")

    return x


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
                path.append(board.dict_of_64_squares[letter_index_to_letter(x1) + str(y)])
                y += 1
    elif y1 == y2:
        # Same row
        x = min(x1,x2) + 1
        while True:
            if x == max(x1,x2):
                # Reached the end of the path.
                break
            else:
                path.append(board.dict_of_64_squares[letter_index_to_letter(x) + str(y1)])
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
                    path.append(board.dict_of_64_squares[letter_index_to_letter(x) + str(y)])
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
                    path.append(board.dict_of_64_squares[letter_index_to_letter(x) + str(y)])
                    x += 1
                    y -= 1
    else:
        # No straight path between squares.
        pass

    return path











def game_loop(current_game):
    """
    This function should be called once per turn (rather than having each turn be a loop iteration).
    This cleans up unused variables after each turn.

    High level approach for each turn:
    - Show user the current board state.
    - Declare whose turn it is.
    - Get user inputs for starting square and ending square, and perform validation types 1 and 2 and 3.
    - Create and instantiate a Turn object.
    - Confirm move is legal using piece-specific logic. [Reject move otherwise, display error text, ask for new inputs]
    - If move is castle-ing, do additional logic to check that it’s valid.
    - Set ending_board attribute.
    - Confirm that King is not put in check by this move. [Reject move otherwise, display error text, ask for new inputs].
    - Set is_check attribute.
    - Set is_checkmate attribute (only if is_check attribute is set to 1 in previous step).
    - Set is_capture attribute.
    - Set notation attribute.
    - Show ending_board to user.
    - Ask user to confirm move. [If rejected, destroy Turn object and return to top step.]
    - If confirmed, do confirmation tasks: 
        Update is_confirmed Turn attribute, 
        Update relevant Piece attributes, 
        Update relevant Square attributes, 
        Update Board is_current attribute, 
        Update Game current_board attribute, 
        Update Player captured_enemy_pieces and points and is_current_turn attributes.

    """


    while True:

        # Show user the current board state
        show_board_state(current_game.current_board, is_current = True)

        # Declare whose turn it is now.
        declare_whose_turn_it_is(current_game.whose_turn)

        # Get validated user inputs.
        source_square, destination_square = get_and_validate_two_user_inputs(current_game)

        # Create and instantiate a Turn object.
        current_turn = Turn(
            starting_board = current_game.current_board, 
            player = current_game.whose_turn, 
            starting_square = source_square, 
            ending_square = destination_square
        )

        # Confirm move is legal for validation type 4.
        if current_turn.is_legal_move_can_reach() is False:
            # Reject move.
            display_error_message(4)
            del current_turn
            continue

        # Confirm move is legal for validation type 5.
        if current_turn.is_legal_move_path_unblocked() is False:
            # Reject move.
            display_error_message(5)
            del current_turn
            continue

        # Confirm move is legal for validation type 6.
        if current_turn.is_legal_move_king_safe() is False:
            # Reject move.
            display_error_message(6)
            del current_turn
            continue

        # Set captured_piece attribute.
        current_turn.set_captured_piece()

        # Show user the proposed board state.
        show_board_state(current_turn.ending_board, is_current = False)

        # Ask user to confirm move.
        if request_user_input_for_move_confirmation() is False:
            # User has cancelled move.
            del current_turn
            continue

        # The move has been confirmed.
        break

    # Now do all the tasks that happen as a result of move confirmation.
    current_game.confirm_turn(current_turn)







def get_and_validate_two_user_inputs(game):
    # Display whose turn it is.
    # Ask for source square input.
    # Retrieve corresponding square and validate it contains player's own piece.
    # Ask for destination square input.
    # Retrieve corresponding square and validate it doesn't contain player's own piece.
    # Return the two square objects.


    while True:

        # Ask user to select a starting square whose occupying piece is to be moved.
        source_input = request_user_input_for_square(source=True)


        # INPUT VALIDATION TYPE 2: Confirm that the source input references a square that contains one of the player's pieces.
        if game.current_board.dict_of_64_squares[source_input].contains_current_players_piece(game.whose_turn) is False:
            # Starting square does not contain a piece belonging to the current player.
            display_error_message(2)
            continue

        # Starting square does contain a piece belonging to the current player.
        source_square = game.current_board.dict_of_64_squares[source_input]
        break



    while True:
        
        # Ask user to select an ending square to move that piece to. 
        destination_input = request_user_input_for_square(source=False)


        # INPUT VALIDATION TYPE 3: Confirm that the destination input references a square that does not contain the current player’s piece (and isn't the same as the source square).
        if game.current_board.dict_of_64_squares[destination_input].contains_current_players_piece(game.whose_turn) is True:
            # Ending square contains a piece belonging to the current player.
            display_error_message(3)
            continue

        # Ending square is does not contain a piece belonging to the current player.
        destination_square = game.current_board.dict_of_64_squares[destination_input]
        break


    return source_square, destination_square




