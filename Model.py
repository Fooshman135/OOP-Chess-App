# Model





class Game:

    # One instance per game.


    def __init__(self, white_player, black_player, current_board):
        self.white_player = white_player
        self.black_player = black_player
        self.current_board = current_board

        self.whose_turn = white_player
        self.list_of_confirmed_turns = []
        


    def confirm_turn(self, confirmed_turn):

        # Update is_confirmed Turn attribute.
        confirmed_turn.is_confirmed = True

        # Add turn to list of confirm turns.
        self.list_of_confirmed_turns.append(confirmed_turn)

        # Update Game current_board attribute.
        self.current_board = confirmed_turn.ending_board

        # Update current player's captured enemy pieces and points.
        if confirmed_turn.captured_piece is not None:
            self.whose_turn.captured_enemy_pieces.append(confirmed_turn.captured_piece)
            self.whose_turn.points += confirmed_turn.captured_piece.points

        # Set up next move.
        ## Update is_current_turn for old current player.
        self.whose_turn.is_current_turn = 0

        ## Switch players
        if confirmed_turn.player is white_player:
            self.whose_turn = black_player
        else:
            self.whose_turn = white_player

        ## Update is_current_turn for new current player.
        self.whose_turn.is_current_turn = 1
        



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




class Board(object):

    def __init__(self, dict_of_64_squares, is_current, whose_turn):
        self.dict_of_64_squares = dict_of_64_squares
        self.is_current = is_current        # A bool        # Is this attribute necessary?
        self.whose_turn = whose_turn        # A Player object



    def duplicate_board(self):
        from copy import deepcopy
        return deepcopy(self)



    def is_king_not_in_check(self, king_color):
        # INPUT VALIDATION TYPE 6: Check to make sure that the move doesn't result in your King being put in check.

        # self is a board in a state that you want to examine to see if the king is in check.
        # king_color identifies which King you want to examine. Values can be either 0 or 1.
        # Returns bool depending on whether the proposed board has your king in check.

        # First, identify all pieces of the opposite color as the king.
        opponents_pieces = []

        for square in self.dict_of_64_squares.values():
            if square.current_occupant is not None:
                if square.current_occupant.owner.color != king_color:
                    # square has one of opponents pieces on it.
                    opponents_pieces.append(square.current_occupant)
                elif isinstance(square.current_occupant, King):
                    # This is the square that your King is on.
                    king_square = square

        if len(opponents_pieces) == 0:
            raise Exception("This is an error!")

        # Then loop through them and see if any of them can directly attack the king.
        for threat in opponents_pieces:
            # threat is a Piece object.
            if threat.target_can_be_reached(king_square) is True:
                if threat.path_to_target_is_unblocked(king_square, self) is True:
                    # Your King can be attacked by this opponent's piece.
                    return False

        return True






class Turn:

    # One instance created per player per turn.
    # This class can be used for hypothetical turns as well (meaning turns which haven't been confirmed yet).

    # The is_capture attribute is a bool of signaling whether the turn involving capturing an enemy piece.
    # The is_confirmed attribute is a bool for signaling whether the turn was actually taken by the player.
    # The is_check attribute is a bool for signaling whether the turn puts the opponent's King in check.
    # The is_checkmate attribute is a bool for signaling whether the turn puts the opponent's King in checkmate.

    def __init__(self, starting_board, player, starting_square, ending_square):
        self.starting_board = starting_board
        self.player = player
        self.starting_square = starting_square
        self.ending_square = ending_square

        self.ordinal_number = None
        self.ending_board = None
        self.notation = None
        self.is_confirmed = False   # Is this attribute necessary?
        self.captured_piece = None
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

        # First create the proposed board.
        if self.ending_board is None:
            self.set_ending_board()
        # Then check the proposed board for putting your King in check.
        return self.ending_board.is_king_not_in_check(self.player.color)




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


    def set_captured_piece(self):
        if self.ending_square.current_occupant is not None and self.ending_square.current_occupant.owner.color != self.player.color:
            self.captured_piece = self.ending_square.current_occupant



    def set_is_check(self):
        other_players_color = (self.player.color + 1) % 2
        self.is_check = not(self.ending_board.is_king_not_in_check(other_players_color))


    def set_is_checkmate(self):

        # First confirm that the opponents King is in check.
        if self.is_check is False:
            return False

        # Now check every move that the opponent can perform and confirm if any of them can get the King out of check.
        pass    #TODO


    def set_notation(self):
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
        if self.owner.color == 0:
            # Black
            self.unicode = "♙"
        else:
            # White
            self.unicode = "♟"

        self.turn_captured = None
        self.points = 1

        




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






class Rook(Piece):

    def __init__(self, current_square, owner):
        self.current_square = current_square
        self.owner = owner  # Should be a Player object.
        if self.owner.color == 0:
            # Black
            self.unicode = "♖"
        else:
            # White
            self.unicode = "♜"

        self.turn_captured = None 
        self.points = 5




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
        if self.owner.color == 0:
            # Black
            self.unicode = "♘"
        else:
            # White
            self.unicode = "♞"

        self.turn_captured = None 
        self.points = 3
        



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
        if self.owner.color == 0:
            # Black
            self.unicode = "♗"
        else:
            # White
            self.unicode = "♝"
        
        self.turn_captured = None 
        self.points = 3


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
        if self.owner.color == 0:
            # Black
            self.unicode = "♕"
        else:
            # White
            self.unicode = "♛"
        
        self.turn_captured = None 
        self.points = 9


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


