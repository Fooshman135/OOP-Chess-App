# Model





class Game:

    # One instance per game.


    def __init__(self, white_player, black_player, current_board):
        self.white_player = white_player
        self.black_player = black_player
        self.current_board = current_board

        self.whose_turn = white_player
        self.list_of_confirmed_turns = []
        






class Player:

    def __init__(self,color):
        self.color = color    # This should be either 0 or 1.

        self.points = 0
        self.captured_enemy_pieces = []
        
        # The is_current_turn attribute may not be necessary.
        if color == 0:
            # Black
            self.is_current_turn = 0
        else:
            # White
            self.is_current_turn = 1






class Square(object):

    def __init__(self, letter_index, number_index, square_color):
        self.letter_index = letter_index
        self.number_index = number_index
        self.square_color = square_color
        self.current_occupant = None


    # letter_index: A = 1, B = 2, ..., H = 8
    # color: White = 1, Black = 2
    # current_occupant: Points to a Piece object



    def contains_current_players_piece(self, current_player):
        # Used for INPUT VALIDATION TYPES 2 and 3.
        # Returns True if current_occupant belong's to the player whose turn it is now.
        if self.current_occupant is None:
            return False
        elif self.current_occupant.owner.color != current_player.color:
            return False
        else:
            return True







    def get_threats(self):
        # Return the set of opponents pieces (or squares?) that can attack this square.
        pass    #TODO






class Board(object):

    def __init__(self, dict_of_64_squares, is_current, whose_turn):
        self.dict_of_64_squares = dict_of_64_squares
        self.is_current = is_current        # A bool
        self.whose_turn = whose_turn        # A Player object



    def duplicate_board(self):
        from copy import deepcopy
        return deepcopy(self)



    def is_king_in_check(self, king_color):
        # Used for INPUT VALIDATION TYPE 6

        # self is a board in a state that you want to examine to see if the king is in check.
        # king_color identifies which King you want to examine. Values can be either 0 or 1.
        # Returns bool depending on whether the proposed board has your king in check.

        pass    # TODO






class Turn:

    # One instance created per player per turn.
    # This class can be used for hypothetical turns as well (meaning turns which haven't been confirmed yet).

    # The is_capture attribute is a bool of signaling whether the turn involving capturing an enemy piece.
    # The is_confirmed attribute is a bool for signaling whether the turn was actually taken by the player.

    def __init__(self, starting_board, player, starting_square, ending_square):
        self.starting_board = starting_board
        self.player = player
        self.starting_square = starting_square
        self.ending_square = ending_square

        self.ordinal_number = None
        self.ending_board = None
        self.notation = None
        self.is_confirmed = False
        self.is_capture = None
        self.is_check = None
        self.is_checkmate = None




    def is_legal_move_can_reach(self):
        # Used for INPUT VALIDATION TYPE 4
        return self.starting_square.current_occupant.target_can_be_reached(self.ending_square)



    def is_legal_move_path_unblocked(self):
        # Used for INPUT VALIDATION TYPE 5
        return self.starting_square.current_occupant.path_to_target_is_unblocked(self.ending_square, self.starting_board)



    def is_legal_move_king_safe(self):
        # Used for INPUT VALIDATION TYPE 6

        # INPUT VALIDATION TYPE 6: Check to make sure that the move doesn't result in your King being put in check.
        # First create the proposed board.
        if self.ending_board is None:
            self.set_ending_board()
        # Then check the proposed board for putting your King in check.
        if self.ending_board.is_king_in_check(self.player.color) is True:
            return False
        else:
            return True




    def set_ending_board(self):
        # This method returns a new board object that is the result of taking this turn.
        # This method should not worry about game logic or turn legality.

        from Services import letter_index_to_letter

        # Create a new board object which is the same as the inital board object. We will return this new board later.
        new_board = self.starting_board.duplicate_board()

        # Update the turn's starting square on the board.
        new_board.dict_of_64_squares[
            letter_index_to_letter(self.starting_square.letter_index) + str(self.starting_square.number_index)
        ].current_occupant = None

        # Update the turn's ending square on the board.
        new_board.dict_of_64_squares[
            letter_index_to_letter(self.ending_square.letter_index) + str(self.ending_square.number_index)
        ].current_occupant = self.starting_square.current_occupant

        # Set the updated board as the ending_board.
        self.ending_board = new_board



    def set_ordinal_number(self):
        pass    #TODO


    def set_is_capture(self):
        pass    #TODO


    def set_is_check(self):
        pass    #TODO


    def set_is_checkmate(self):
        pass    #TODO


    def set_notation(self):
        pass    #TODO


    def confirm(self):
        pass    #TODO







class Piece(object):


    def path_to_target_is_unblocked(self, target_square, board):
        # INPUT VALIDATION TYPE 5: Check to see if any square along the path is occupied.

        from Services import produce_path_between_two_squares
        path = produce_path_between_two_squares(self.current_square, target_square, board)
        if len(path) == 0:
            # There is no path, and so nothing is blocked.
            pass
        else:
            # There is a path, so need to check each square in the path.
            for square in path:
                if square.current_occupant is not None:
                    return False
        return True




class Pawn(Piece):

    def __init__(self, current_square, owner):
        self.current_square = current_square
        self.owner = owner  # Should be a Player object.
        self.turn_captured = None
        if self.owner.color == 0:
            # Black
            self.unicode = "♙"
        else:
            # White
            self.unicode = "♟"
        




    def target_can_be_reached(self, target_square):
        # INPUT VALIDATION TYPE 4: Check to see if the target square can be reached, assuming an empty board.

        x1 = self.current_square.letter_index
        y1 = self.current_square.number_index
        x2 = target_square.letter_index
        y2 = target_square.number_index

        if self.owner.color == 1:
            # White pawns
            if x1 == x2 and y2 == y1 + 1:
                return True
            elif x1 == x2 and y1 == 2 and y2 == 4:
                return True
            elif abs(x2 - x1) == 1 and y2 == y1 + 1 and target_square.current_occupant.owner.color == 0:
                return True
            else:
                return False
        elif self.owner.color == 0:
            # Black pawns
            if x1 == x2 and y2 == y1 - 1:
                return True
            elif x1 == x2 and y1 == 7 and y2 == 5:
                return True
            elif abs(x2 - x1) == 1 and y2 == y1 - 1 and target_square.current_occupant.owner.color == 1:
                return True
            else:
                return False
        else:
            # Throw error
            raise Exception("This is an error!")




    def check_for_promotion(self):
        # Checks to see if the pawn can be promoted.
        pass    #TODO



    def get_moves(self):
        pass    #TODO


    def get_attacks(self):
        # Returns a list of squares (or pieces?) that this piece can move to in an attack.
        pass    #TODO






class Rook(Piece):

    def __init__(self, current_square, owner):
        self.current_square = current_square
        self.owner = owner  # Should be a Player object.
        self.turn_captured = None
        if self.owner.color == 0:
            # Black
            self.unicode = "♖"
        else:
            # White
            self.unicode = "♜"
        



    def target_can_be_reached(self, target_square):
        # INPUT VALIDATION TYPE 4: Check to see if the target square can be reached, assuming an empty board.

        x1 = self.current_square.letter_index
        y1 = self.current_square.number_index
        x2 = target_square.letter_index
        y2 = target_square.number_index


        if x1 == x2 or y1 == y2:
            return True
        else:
            return False





class Knight(Piece):

    def __init__(self, current_square, owner):
        self.current_square = current_square
        self.owner = owner  # Should be a Player object.
        self.turn_captured = None
        if self.owner.color == 0:
            # Black
            self.unicode = "♘"
        else:
            # White
            self.unicode = "♞"
        



    def target_can_be_reached(self, target_square):
        # INPUT VALIDATION TYPE 4: Check to see if the target square can be reached, assuming an empty board.

        # Need to confirm that target_square is an L-shaped jump away from the current_square.
        x1 = self.current_square.letter_index
        y1 = self.current_square.number_index
        x2 = target_square.letter_index
        y2 = target_square.number_index


        if (
            (x2 == x1+2 and y2 == y1+1) 
            or (x2 == x1+2 and y2 == y1-1)
            or (x2 == x1+1 and y2 == y1+2)
            or (x2 == x1+1 and y2 == y1-2)
            or (x2 == x1-2 and y2 == y1+1)
            or (x2 == x1-2 and y2 == y1-1)
            or (x2 == x1-1 and y2 == y1+2)
            or (x2 == x1-1 and y2 == y1-2)
        ):
            return True
        else:
            return False
        



    def path_to_target_is_unblocked(self, target_square, board):
        # Used for INPUT VALIDATION TYPE 5
        # The knight's path is never blocked because it leaps over other pieces.
        return True






class Bishop(Piece):

    def __init__(self, current_square, owner):
        self.current_square = current_square
        self.owner = owner  # Should be a Player object.
        self.turn_captured = None
        if self.owner.color == 0:
            # Black
            self.unicode = "♗"
        else:
            # White
            self.unicode = "♝"
        



    def target_can_be_reached(self, target_square):
        # INPUT VALIDATION TYPE 4: Check to see if the target square can be reached, assuming an empty board.

        x1 = self.current_square.letter_index
        y1 = self.current_square.number_index
        x2 = target_square.letter_index
        y2 = target_square.number_index

        if abs(x1 - x2) == abs(y1 - y2):
            return True
        else:
            return False





class Queen(Piece):

    def __init__(self, current_square, owner):
        self.current_square = current_square
        self.owner = owner  # Should be a Player object.
        self.turn_captured = None
        if self.owner.color == 0:
            # Black
            self.unicode = "♕"
        else:
            # White
            self.unicode = "♛"
        



    def target_can_be_reached(self, target_square):
        # INPUT VALIDATION TYPE 4: Check to see if the target square can be reached, assuming an empty board.

        x1 = self.current_square.letter_index
        y1 = self.current_square.number_index
        x2 = target_square.letter_index
        y2 = target_square.number_index

        if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            return True
        else:
            return False





class King(Piece):

    def __init__(self, current_square, owner):
        self.current_square = current_square
        self.owner = owner  # Should be a Player object.
        if self.owner.color == 0:
            # Black
            self.unicode = "♔"
        else:
            # White
            self.unicode = "♚"




    def target_can_be_reached(self, target_square):
        # INPUT VALIDATION TYPE 4: Check to see if the target square can be reached, assuming an empty board.

        # Need to confirm that target_square is one square away from the current_square.
        x1 = self.current_square.letter_index
        y1 = self.current_square.number_index
        x2 = target_square.letter_index
        y2 = target_square.number_index

        if (x2 in [x1 - 1, x1, x1 + 1]) and (y2 in [y1 - 1, y1, y1 + 1]) and ((x2 != x1) or (y2 != y1)):
            return True
        else:
            return False




    def path_to_target_is_unblocked(self, target_square, board):
        # Used for INPUT VALIDATION TYPE 5
        # The king's path is never blocked because he can only move one square.
        return True








    def get_moves(self):


        # Not sure if this method is needed, because I may just have users input the square they want to move into.


        # First, return the set of all squares that the King can move to assuming an empty board.
        # There are 8 logical checks we need to perform, see which are legal squares and which are off the board.



        # Second, filter out squares which already have one of your other pieces on it.



        # Third, filter out squares which put the King in check.


        pass    # TODO








