# Model

# from abc import ABCMeta, abstractmethod



class Square(object):

    def __init__(self, letter_index, number_index, square_color):
        self.letter_index = letter_index
        self.number_index = number_index
        self.square_color = square_color
        self.current_occupant = None


    # letter_index: A = 1, B = 2, ..., H = 8
    # color: White = 1, Black = 2
    # current_occupant: Points to a Piece object



    def get_current_piece(self):
        # Return None if square is not occupied.
        pass


    def set_starting_position_piece(self, my_piece):

        pass




class Board(object):

    def __init__(self, dict_of_64_squares):
        self.dict_of_64_squares = dict_of_64_squares
        self.is_current_state = 0








class Piece(object):


    def get_current_square(self):
        return self.current_square



    def get_threats(self):
        # Return the set of opponents pieces (or squares?) that can attack this piece.
        pass








class Pawn(Piece):

    def __init__(self, current_square, color):
        self.current_square = current_square
        self.color = color  # Should be a Player object.
        if self.color == 0:
            # Black
            self.unicode = "♙"
        else:
            # White
            self.unicode = "♟"
        


    def get_moves(self):
        pass


    def get_attacks(self):
        pass






    def get_unicode_character(self):
        return self.unicode



    def check_for_promotion(self):
        # Checks to see if the pawn can be promoted.
        pass







class Rook(Piece):

    def __init__(self, current_square, color):
        self.current_square = current_square
        self.color = color  # Should be a Player object.
        if self.color == 0:
            # Black
            self.unicode = "♖"
        else:
            # White
            self.unicode = "♜"
        


    def get_moves(self):
        # Return a list of square objects that this piece can move to on this turn.

        # First retrieve the letter_index and the number_index from the current square.
        # Then produce the two indices for each square that this piece could move to assuming an empty board.
        # Then eliminate squares which are blocked by your own pieces or are behind a piece.

        # Finally, determine which of the remaining squares are occupied by an opponent's piece.
        pass



    def is_move_legal(self, target_square):
        # Returns bool depending on whether the piece can legally move into the target square.
        pass




    def get_attacks(self):
        pass






    def get_unicode_character(self):
        return self.unicode






class Knight(Piece):

    def __init__(self, current_square, color):
        self.current_square = current_square
        self.color = color  # Should be a Player object.
        if self.color == 0:
            # Black
            self.unicode = "♘"
        else:
            # White
            self.unicode = "♞"
        





class Bishop(Piece):

    def __init__(self, current_square, color):
        self.current_square = current_square
        self.color = color  # Should be a Player object.
        if self.color == 0:
            # Black
            self.unicode = "♗"
        else:
            # White
            self.unicode = "♝"
        







class Queen(Piece):

    def __init__(self, current_square, color):
        self.current_square = current_square
        self.color = color  # Should be a Player object.
        if self.color == 0:
            # Black
            self.unicode = "♕"
        else:
            # White
            self.unicode = "♛"
        









class King(Piece):

    def __init__(self, current_square, color):
        self.current_square = current_square
        self.color = color  # Should be a Player object.
        if self.color == 0:
            # Black
            self.unicode = "♔"
        else:
            # White
            self.unicode = "♚"




    def get_moves(self):


        # Not sure if this method is needed....


        # First, return the set of all squares that the King can move to assuming an empty board.
        # There are 8 logical checks we need to perform, see which are legal squares and which are off the board.



        # Second, filter out squares which already have one of your other pieces on it.



        # Third, filter out squares which put the King in check.


        pass





        

    def is_move_legal(self, target_square):

        # Returns bool depending on whether the piece can legally move into the target square.


        # First get the current square's indexes and the target square's indexes.
        x1 = self.current_square.letter_index
        y1 = self.current_square.number_index

        x2 = target_square.letter_index
        y2 = target_square.number_index


        # Then check to see if the target square can be reached, assuming an empty board.
        # Need to confirm that target_square is one square away from the current_square.
        if not((x2 in [x1 - 1, x1, x1 + 1]) and (y2 in [y1 - 1, y1, y1 + 1]) and ((x2 != x1) or (y2 != y1))):
            return 0       


        # Then check to see if the target square is occupied by one of your own pieces.
        if target_square.current_occupant != None and target_square.current_occupant.color == self.color:
            return 0           


        # Then check to see if any square along the way is occupied.
        # This step is not needed for the King!


        # Finally, check to make sure that moving there doesn't result in your King being put in check.
        # new_board = 

        if is_king_in_check(new_board) == 1:
            return 0


        # If you've reached this point, then the move is legal!
        return 1

        






    def is_king_in_check(self, proposed_board):
        # proposed_board is a board in a state that you want to examine if the king is in check.
        # Returns bool depending on whether the proposed board has your king in check.

        pass









class Player:

    def __init__(self,color, points):
        self.color = color









class Turn:

    # One instance created per player per turn.

    def __init__(self, ordinal_number, player, piece, starting_square, ending_square, notation):
        pass







