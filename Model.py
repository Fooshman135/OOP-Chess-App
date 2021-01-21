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
            self.unicode = ♙
        else:
            # White
            self.unicode = ♟
        


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
            self.unicode = ♖
        else:
            # White
            self.unicode = ♜
        


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
            self.unicode = ♘
        else:
            # White
            self.unicode = ♞
        





class Bishop(Piece):

    def __init__(self, current_square, color):
        self.current_square = current_square
        self.color = color  # Should be a Player object.
        if self.color == 0:
            # Black
            self.unicode = ♗
        else:
            # White
            self.unicode = ♝
        





class King(Piece):

    def __init__(self, current_square, color):
        self.current_square = current_square
        self.color = color  # Should be a Player object.
        if self.color == 0:
            # Black
            self.unicode = ♔
        else:
            # White
            self.unicode = ♚
        





class Queen(Piece):

    def __init__(self, current_square, color):
        self.current_square = current_square
        self.color = color  # Should be a Player object.
        if self.color == 0:
            # Black
            self.unicode = ♕
        else:
            # White
            self.unicode = ♛
        







class Player:

    def __init__(self,color, points):
        self.color = color









class Turn:

    # One instance created per player per turn.

    def __init__(self, ordinal_number, player, piece, starting_square, ending_square, notation):
        pass







