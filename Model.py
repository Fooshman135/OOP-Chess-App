# Model





class Game:

    # One instance per game.


    def __init__(self, white_player, black_player, list_of_confirmed_turns, current_board):
        self.white_player = white_player
        self.black_player = black_player
        self.list_of_confirmed_turns = list_of_confirmed_turns
        self.current_board = current_board






class Player:

    def __init__(self,color):
        self.color = color
        self.points = 0
        self.captured_enemy_pieces = []







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







class Board(object):

    def __init__(self, dict_of_64_squares, is_current, whose_turn):
        self.dict_of_64_squares = dict_of_64_squares
        self.is_current = is_current
        self.whose_turn = whose_turn



    def duplicate_board(self):
        return Board(se.f.dict_of_64_squares, self.is_current, self.whose_turn)








class Turn:

    # One instance created per player per turn.
    # Maybe this class can be used for hypothetical turns as well.

    # The is_capture attribute is a bool of signaling whether the turn involving capturing an enemy piece.
    # The is_confirmed attribute is a bool for signaling whether the turn was actually taken by the player.

    def __init__(self, ordinal_number, starting_board, player, starting_square, ending_square):
        self.ordinal_number = ordinal_number
        self.starting_board = starting_board
        self.player = player
        self.starting_square = starting_square
        self.ending_square = ending_square

        self.ending_board = None
        self.notation = None
        self.is_confirmed = 0
        self.is_capture = None




    def is_legal_move(self):
        pass




    def create_new_board_from_turn(self):
        # This function takes an initial board object and a turn object, and it returns a new board object that is the result of taking that turn.
        # This function should not worry about game logic or turn legality.


        # Create a new board object which is the same as the inital board object. We will return this new board later.
        new_board = self.starting_board.duplicate_board()

        # Update the turn's starting square on the board.
        # First get the starting square from the turn.
        # Then find the analogous square in the board.
        # Then set that square's occupant to be None.
        new_board.dict_of_64_squares[
            letter_index_to_letter(self.starting_square.letter_index) + str(self.starting_square.number_index)
        ].current_occupant = None

        # Update the turn's ending square on the board.
        new_board.dict_of_64_squares[
            letter_index_to_letter(self.ending_square.letter_index) + str(self.ending_square.number_index)
        ].current_occupant = self.starting_square.current_occupant

        # Set the updated board as the ending_board.
        self.ending_board = new_board



    def set_notation(self):
        pass



    def set_is_capture(self):
        pass



    def confirm(self):
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
        self.turn_captured = None
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
        self.turn_captured = None
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
        self.turn_captured = None
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
        self.turn_captured = None
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
        self.turn_captured = None
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


        # Not sure if this method is needed, because I may just have users input the square they want to move into.


        # First, return the set of all squares that the King can move to assuming an empty board.
        # There are 8 logical checks we need to perform, see which are legal squares and which are off the board.



        # Second, filter out squares which already have one of your other pieces on it.



        # Third, filter out squares which put the King in check.


        pass




    def is_move_legal(self, target_square):

        # Returns bool depending on whether the piece can legally move into the target square.

        # SHOULD THIS BE A TURN METHOD INSTEAD OF A KING METHOD?


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











