# View

from Model import *
from Globals import *







def print_text_to_cli(display_text):

    print("{}\n".format(display_text))



def get_text_input_from_cli(prompt):
    try:
        user_input = raw_input(prompt).strip()    # Python 2.X
    except NameError:
        user_input = input(prompt).strip()      # Python 3.X
    return user_input




def press_key_to_continue():
    """Prompts the user to hit a button before displaying the next menu."""

    if GUI is False:
        #CLI
        
        message = "Press Enter to continue... "
        get_text_input_from_cli(message)
        print_text_to_cli("")           # Prints a blank line.

    else:
        #GUI
        pass    #TODO



def show_current_board_state(board):

    if GUI is False:
        # CLI

        message = "Here is what the board currently looks like:"
        print_text_to_cli(message)

        print_board_cli(board, white_on_bottom=WHITE_ON_BOTTOM)

    else:
        #GUI
        pass    #TODO




def declare_whose_turn_it_is(whose_turn):

    if GUI is False:
        #CLI

        from Services import color_number_to_text

        message = "\nIt is now {}'s turn!".format(color_number_to_text(whose_turn.color))
        print_text_to_cli(message)

    else:
        #GUI
        pass    #TODO




def request_user_input_for_square(source):

    # whose_turn is the Player whose turn it is.
    # source is a bool. True means it's a source square. False means it's a destination square.

    if GUI is False:
        #CLI


        if source is True:
            prompt = "Type in the square containing the piece you want to move (such as 'e2'): "
        else:
            prompt = "Now type in the square that you want to move the selected piece to (such as 'e4'): "


        while True:

            square_input = get_text_input_from_cli(prompt)

            # INPUT VALIDATION TYPE 1: Is the syntax valid? Does it actually identify one of the 64 possible squares?
            if validate_user_input_square_selection(square_input) is False:
                # Input was invalid.
                display_error_message(1)
                continue

            # Input was valid.
            return square_input

    else:
        #GUI
        pass    #TODO







def validate_user_input_square_selection(user_input):
    # Used for INPUT VALIDATION TYPE 1.
    # Confirm that user_input uniquely identifies a square on the board.
    # user_input should be a string.


    # Test 1: String should be only two characters.
    if len(user_input) != 2:
        return False

    # Test 2: First character should be a letter between a and h inclusive.
    if user_input[0] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        return False

    # Test 3: Second character should be a number between 1 and 8 inclusive.
    if user_input[1] not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        return False

    # If all tests pass, the input is valid.
    return True





def display_error_message(error_type):

    if GUI is False:
        #CLI

        if error_type == 1:
            message = "\nInvalid input: Doesn't map to a square on the board."
        elif error_type == 2:
            message = "\nInvalid input: Starting square doesn't contain one of your pieces."
        elif error_type == 3:
            message = "\nInvalid input: Ending square contains one of your pieces."
        elif error_type == 4:
            message = "\nInvalid input: Ending square is out of reach for this piece."
        elif error_type == 5:
            message = "\nInvalid input: Path to ending square is blocked."
        elif error_type == 6:
            message = "\nInvalid input: This move would put your own king in check."

        print_text_to_cli(message)
        press_key_to_continue()


    else:
        #GUI
        pass    #TODO




def print_board_cli(board, white_on_bottom = True):
    # board is a dictionary of 64 square objects.
    # white_on_bottom is True if the white player is displayed on the bottom and the black player is displayed on the top. False otherwise.

    from Services import letter_index_to_letter

    # The following dictionary comprehension assigns a space to empty squares, and assigns the piece's unicode to occupied squares.
    unicode_dict = {k: (" " if v.current_occupant == None else v.current_occupant.unicode) for (k,v) in board.dict_of_64_squares.items()}

    # Now produce the strings used to show the board.
 
    horizontal_line =  "    _________________________________"

    if white_on_bottom is True:
        outer_range = range(8,0,-1)
        inner_range = range(1,9)
        title = "      a   b   c   d   e   f   g   h  "
    else:
        outer_range = range(1,9)
        inner_range = range(8,0,-1)
        title = "      h   g   f   e   d   c   b   a  "

    print(title)

    for number_index in outer_range:
        print(horizontal_line)
        square_index = []
        for letter_index in inner_range:
            square_index.append(letter_index_to_letter(letter_index) + str(number_index))

        row = "{number}   | {a} | {b} | {c} | {d} | {e} | {f} | {g} | {h} |".format(
            number = number_index,
            a = unicode_dict[square_index[0]], b = unicode_dict[square_index[1]],
            c = unicode_dict[square_index[2]], d = unicode_dict[square_index[3]],
            e = unicode_dict[square_index[4]], f = unicode_dict[square_index[5]],
            g = unicode_dict[square_index[6]], h = unicode_dict[square_index[7]]
            )
        print(row)

    print(title)

