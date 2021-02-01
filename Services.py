# Services

from Model import *



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

    # IS THIS NEEDED ANYMORE NOW THAT WE USE DICTIONARIES INSTEAD OF LISTS?
    
    x = None

    for i in range(len(array_of_squares)):
        if (array_of_squares[i].letter_index == letter_index_here and array_of_squares[i].number_index == number_index_here):
            x = array_of_squares[i]
            break

    if x is None:
        # Throw error
        raise Exception("This is an error!")

    return x




def generate_empty_board():

    # Generate the empty board by instantiating 64 Square objects and return them in a dictionary.

    dict_of_squares = {}
    color = 1

    for letter_index in range(1,9):
        color += 1      # Flip the square color back (every time we increment the row).
        for number_index in range(1,9):
            dict_of_squares[letter_index_to_letter(letter_index) + str(number_index)] = Square(letter_index, number_index, color_number_to_text(color % 2))
            color += 1      # Flip the square color

    return dict_of_squares






def pieces_into_starting_positions(board, white_player, black_player):
    # This function assigns a piece to each Square as the starting position.
    # board is a dictionary of Square objects.
    # It is not necessary for all the Square objects in board to be empty, as they will be overwritten.
    

    for square in board.values():

        if square.number_index == 1:
            if square.letter_index == 1 or square.letter_index == 8:
                square.current_occupant = Rook(square, white_player)           # White rooks
            elif square.letter_index == 2 or square.letter_index == 7:
                square.current_occupant = Knight(square, white_player)         # White knights
            elif square.letter_index == 3 or square.letter_index == 6:
                square.current_occupant = Bishop(square, white_player)         # White bishops
            elif square.letter_index == 4:
                square.current_occupant = Queen(square, white_player)          # White queen
            elif square.letter_index == 5:
                square.current_occupant = King(square, white_player)           # White king 
            else:
                raise Exception("This is an error!")         
        
        elif square.number_index == 2:
            square.current_occupant = Pawn(square, white_player)               # White pawns

        elif square.number_index == 7:
            square.current_occupant = Pawn(square, black_player)               # Black pawns

        elif square.number_index == 8:
            if square.letter_index == 1 or square.letter_index == 8:
                square.current_occupant = Rook(square, black_player)           # Black rooks
            elif square.letter_index == 2 or square.letter_index == 7:
                square.current_occupant = Knight(square, black_player)         # Black knights
            elif square.letter_index == 3 or square.letter_index == 6:
                square.current_occupant = Bishop(square, black_player)         # Black bishops
            elif square.letter_index == 4:
                square.current_occupant = Queen(square, black_player)          # Black queen
            elif square.letter_index == 5:
                square.current_occupant = King(square, black_player)           # Black king   
            else:
                raise Exception("This is an error!")    
        else:
            pass










