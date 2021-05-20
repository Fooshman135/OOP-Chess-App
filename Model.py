# Model

from Services import *
from View import *



class Game(object):

    def __init__(self):
        self.white_player = Player(1)
        self.black_player = Player(0)
        self.current_board = Board()
        self.current_board.pieces_into_starting_positions(self.white_player, self.black_player)
        self.whose_turn = self.white_player
        self.list_of_confirmed_turns = []
        self.checkmate_achieved = False
        self.stalemate_achieved = False
        


    def game_loop(self):

        while True:
            self.game_turn_loop()
            if self.checkmate_achieved is True or self.stalemate_achieved is True:
                break

        # The game is over because one player checkmated the other or stalemate was reached.
        declare_game_over(self)



    def game_turn_loop(self):
        """

        This function should be called once per turn (rather than having each turn be a loop iteration).
        This cleans up unused variables after each turn.

        """

        # Flip global variable WHITE_ON_BOTTOM
        set_global_white_on_bottom(self.whose_turn.color)


        while True:

            # Show user the current board state
            show_board_state(self.current_board, is_current = True)

            # Declare whose turn it is now.
            declare_whose_turn_it_is(self.whose_turn)

            # Get validated user input for source square.
            source_square = get_and_validate_user_input(self, True)

            while True:

                # Get validated user input for destination square.
                destination_square = get_and_validate_user_input(self, False)
                if isinstance(destination_square, Board.Square) is False:
                    # User has cancelled selecting destination square.
                    break

                # Create and instantiate a Turn object.
                current_turn = Turn(
                    starting_board = self.current_board, 
                    player = self.whose_turn, 
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

                # Break out of inner loop.
                break

            # Check to see if user cancelled selecting destination square.
            if isinstance(destination_square, Board.Square) is False:
                # User has cancelled selecting destination square.
                # Go to top of outer loop.
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
        self.confirm_turn(current_turn)


        # Determine whether endgame has been achieved.
        self.determine_if_endgame()



    def confirm_turn(self, confirmed_turn):

        # Set ordinal_number.
        confirmed_turn.set_ordinal_number(self.list_of_confirmed_turns)

        # Add turn to list of confirm turns.
        self.list_of_confirmed_turns.append(confirmed_turn)

        # Update Game current_board attribute.
        self.current_board = confirmed_turn.ending_board

        # Update the moved piece's location.
        confirmed_turn.starting_square.current_occupant.current_square = confirmed_turn.ending_square

        # Update the moved piece's has_moved_previously attribute.
        if confirmed_turn.starting_square.current_occupant.has_moved_previously is False:
            confirmed_turn.starting_square.current_occupant.has_moved_previously = True

        # Update current player's captured enemy pieces and points.
        if confirmed_turn.captured_piece is not None:
            self.whose_turn.captured_enemy_pieces.append(confirmed_turn.captured_piece)
            self.whose_turn.points += confirmed_turn.captured_piece.points

        # Switch players
        self.whose_turn = self.get_other_player()
        


    def determine_if_endgame(self):

        # This method checks for stalemate and checkmate conditions, and then sets the checkmate_achieved attribute or the stalemate_achieved attribute accordingly.

        # First see if any piece can move.
        if self.can_any_piece_legally_move() is False:
            # No piece can move, so endgame as been achieved.
            # But is it checkmate or stalemate?
            if self.current_board.is_king_not_in_check(self.whose_turn.color) is True:
                # The King is not in check.
                self.stalemate_achieved = True
            else:
                # The King is in check.
                self.checkmate_achieved = True



    def can_any_piece_legally_move(self):

        # Returns True if at least one piece can move, False otherwise.


        ## Produce a list of all squares containing pieces belonging to the current player.
        ## This essentially performs validation types 1 and 2.
        list_of_piece_squares = []
        for square in self.current_board.dict_of_64_squares.values():
            if square.current_occupant is not None and square.current_occupant.owner.color == self.whose_turn.color:
                # Square contains current player's piece.
                list_of_piece_squares.append(square)


        ## For each piece, iterate over every square on the board and see if that piece can legally move to that square and get the King out of check.
        for source_square in list_of_piece_squares:
            for destination_square in self.current_board.dict_of_64_squares.values():
                # Determine whether the selected piece can legally move to the selected square.

                ## Confirm move is legal for validation type 3.
                if destination_square.contains_specified_players_piece(self.whose_turn) is True:
                    # Reject this iteration.
                    continue

                ## Create and instantiate a Turn object.
                current_turn = Turn(
                    starting_board = self.current_board, 
                    player = self.whose_turn, 
                    starting_square = source_square, 
                    ending_square = destination_square
                )

                ## Confirm move is legal for validation type 4.
                if current_turn.is_legal_move_can_reach() is False:
                    # Reject this iteration.
                    del current_turn
                    continue

                ## Confirm move is legal for validation type 5.
                if current_turn.is_legal_move_path_unblocked() is False:
                    # Reject this iteration.
                    del current_turn
                    continue

                ## Confirm move is legal for validation type 6.
                if current_turn.is_legal_move_king_safe() is False:
                    # Reject this iteration.
                    del current_turn
                    continue

                # If you reach this point, then this move is legal so this piece can move.
                return True

        # If you reach this point, then all moves are illegal and therefore no piece can move.
        return False


  
    def get_other_player(self):
        # Return the Player object for the player whose turn is not right now.

        if self.whose_turn is self.white_player:
            return self.black_player
        else:
            return self.white_player



class Player(object):

    def __init__(self, color):
        self.color = color    # This should be either 0 or 1.

        self.points = 0
        self.captured_enemy_pieces = []


    def get_opponents_color_index(self):
        return (self.color + 1) % 2



class Board(object):


    class Square(object):

        def __init__(self, letter_index, number_index, square_color):
            self.letter_index = letter_index    # A = 1, B = 2, ..., H = 8
            self.number_index = number_index
            self.square_color = square_color    # 1 for White, 0 for Black
            self.current_occupant = None        # Points to a Piece object


        def get_square_index_string(self):
            from Services import square_indices_to_string
            return square_indices_to_string(self.letter_index, self.number_index)


        def contains_specified_players_piece(self, player):
            # Used for INPUT VALIDATION TYPES 2 and 3.
            # Returns True if current_occupant belongs to the player passed in as input.
            if self.current_occupant is None:
                return False
            elif self.current_occupant.owner.color != player.color:
                return False
            else:
                return True



    def __init__(self):
        # Create the 64 square objects that make up the board.
        self.dict_of_64_squares = self.generate_empty_board()



    def generate_empty_board(self):

        # Generate the empty board by instantiating 64 Square objects and return them in a dictionary.

        from Services import square_indices_to_string

        dict_of_squares = {}
        square_color = 1

        for letter_index in range(1,9):
            square_color = (square_color + 1) % 2      # Flip the square color back (every time we increment to the next row).
            for number_index in range(1,9):
                dict_of_squares[square_indices_to_string(letter_index, number_index)] = self.Square(letter_index, number_index, square_color)
                square_color = (square_color + 1) % 2      # Flip the square color as we step along a single row

        return dict_of_squares



    def pieces_into_starting_positions(self, white_player, black_player):
        # This function instantiates all pieces and maps them to their starting position Squares.
        # white_player and black_player are both Player objects.
        

        starting_positions_dict = {
            "a1": Rook(None, white_player),
            "b1": Knight(None, white_player),
            "c1": Bishop(None, white_player),
            "d1": Queen(None, white_player),
            "e1": King(None, white_player),
            "f1": Bishop(None, white_player),
            "g1": Knight(None, white_player),
            "h1": Rook(None, white_player),

            "a2": Pawn(None, white_player),
            "b2": Pawn(None, white_player),
            "c2": Pawn(None, white_player),
            "d2": Pawn(None, white_player),
            "e2": Pawn(None, white_player),
            "f2": Pawn(None, white_player),
            "g2": Pawn(None, white_player),
            "h2": Pawn(None, white_player),

            "a7": Pawn(None, black_player),
            "b7": Pawn(None, black_player),
            "c7": Pawn(None, black_player),
            "d7": Pawn(None, black_player),
            "e7": Pawn(None, black_player),
            "f7": Pawn(None, black_player),
            "g7": Pawn(None, black_player),
            "h7": Pawn(None, black_player),

            "a8": Rook(None, black_player),
            "b8": Knight(None, black_player),
            "c8": Bishop(None, black_player),
            "d8": Queen(None, black_player),
            "e8": King(None, black_player),
            "f8": Bishop(None, black_player),
            "g8": Knight(None, black_player),
            "h8": Rook(None, black_player),
        }

        self.pieces_into_specified_positions(starting_positions_dict)



    def pieces_into_specified_positions(self, dict_of_squares_and_pieces):
        # dict_of_squares_and_pieces is a dictionary whose keys are strings specifying squares and whose values are Piece objects.
        # This method maps the pieces to the square objects, and maps the square objects to the pieces.

        # First clear the board of any old pieces.
        for square in self.dict_of_64_squares.values():
            square.current_occupant = None

        # Now assign the new pieces.
        for k,v in dict_of_squares_and_pieces.items():
            self.dict_of_64_squares[k].current_occupant = v
            v.current_square = self.dict_of_64_squares[k]



    def duplicate_board(self):
        from copy import deepcopy
        return deepcopy(self)



    def is_king_not_in_check(self, king_color):
        # INPUT VALIDATION TYPE 6: Check to make sure that the move doesn't result in your King being put in check.

        # self is a board in a state that you want to examine to see if the king is in check.
        # king_color identifies which King you want to examine. Values can be either 0 or 1.
        # Returns bool depending on whether the proposed board has that king in check.

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
            ###print("\nCan {x} attack the King?".format(x=threat.__class__.__name__))
            if threat.target_can_be_reached(king_square) is True:
                ###print("{x} can reach the King".format(x=threat.__class__.__name__))
                if threat.path_to_target_is_unblocked(king_square, self) is True:
                    # Your King can be attacked by this opponent's piece.
                    ###print("AND {x} has an unblocked path to the King. FAILED check 6.".format(x=threat.__class__.__name__))
                    return False
                ###else:
                    ###print("...but {x} has a blocked path.".format(x=threat.__class__.__name__))
            ###else:
                ###print("Nope, {x} cannot reach the King".format(x=threat.__class__.__name__))

        ###print("\nPassed check 6")
        return True



class Turn(object):

    # One instance created per player per turn.
    # This class can be used for hypothetical turns as well (meaning turns which haven't been confirmed yet).

    # The is_capture attribute is a bool of signaling whether the turn involving capturing an enemy piece.
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
        self.captured_piece = None
        self.is_check = None
        self.is_checkmate = None
        self.is_promotion = False



    def is_legal_move_castling(self):
        # Returns True if the move is legal for castling, False otherwise.

        # Need to confirm each of the following:
        # (1) Starting square contains a King (don't need to check color because that was done previously).
        # (2) King hasn't moved previously.
        # (3) Ending square is in the same row as starting square (this is first half of INPUT VALIDATION TYPE 4).
        # (4) Ending square is two squares away from starting square (this is second half of INPUT VALIDATION TYPE 4).
        # (5) Path between King and ending square is not blocked (this is INPUT VALIDATION TYPE 5).
        # (6) The final square beyond the ending square contains a Rook.
        # (7) Rook hasn't moved previously.
        # (8) Path between Rook and ending square is not blocked.
        # (9) King is not currently in check.
        # (10) King does not pass through check in the one square on the path.


        from Services import produce_path_between_two_squares, square_indices_to_string


        # (1)
        if isinstance(self.starting_square.current_occupant, King) is False:
            # The piece on the starting square is not a King.
            return False

        # (2)
        if self.starting_square.current_occupant.has_moved_previously is True:
            # The King was moved in a previous turn.
            return False

        # (3)
        if self.starting_square.number_index != self.ending_square.number_index:
            # Ending square is not in same row as starting square.
            return False

        # (4)
        king_path = produce_path_between_two_squares(self.starting_square, self.ending_square, self.starting_board)
        if len(king_path) != 1:
            # Ending square is either too close or too far away.
            return False

        # (5)
        if king_path[0].current_occupant is not None:
            # Path between King and ending square is blocked.
            return False

        # (6)
        if self.starting_square.letter_index < self.ending_square.letter_index:
            # King side castle
            rook_letter_index = 8
        else:
            # Queen side castle
            rook_letter_index = 1            
        rook_square = self.starting_board.dict_of_64_squares[square_indices_to_string(rook_letter_index, self.starting_square.number_index)]
        if rook_square.current_occupant is None or isinstance(rook_square.current_occupant, Rook) is False:
            # The final square doesn't contain a Rook.
            return False

        # (7)
        if rook_square.current_occupant.has_moved_previously is True:
            # The Rook was moved in a previous turn.
            return False

        # (8)
        rook_path = produce_path_between_two_squares(rook_square, self.ending_square, self.starting_board)
        for square in rook_path:
            if square.current_occupant is not None:
                # Path between Rook and ending square is blocked.
                return False

        # (9)
        if self.starting_board.is_king_not_in_check(self.player.color) is False:
            # King is currently in check.
            return False

        # (10)
        ## Create a new board that is the result of moving the King into the one square in king_path
        new_board = self.starting_board.duplicate_board()
        new_board.dict_of_64_squares[self.starting_square.get_square_index_string()].current_occupant = None
        new_board.dict_of_64_squares[king_path[0].get_square_index_string()].current_occupant = self.starting_square.current_occupant
        ## Now determine if the King is in check while in this square.
        if new_board.is_king_not_in_check(self.player.color) is False:
            # King would pass through check while castling.
            return False

        # If you have reached this point, the move is a legal castling.
        return True



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

        # Create a new board object which is the same as the inital board object. We will return this new board later.
        new_board = self.starting_board.duplicate_board()

        # Update the turn's starting square on the board.
        new_board.dict_of_64_squares[self.starting_square.get_square_index_string()].current_occupant = None


        # Update the turn's ending square on the board.
        self.set_is_promotion()
        if self.is_promotion is True:
            # A pawn is to be promoted, so ending square should contain promoted piece instead of pawn.
            promotion_piece_code = request_user_input_for_promotion()
            if promotion_piece_code in ('q'):
                promotion_piece = Queen(self.ending_square, self.player)
            elif promotion_piece_code in ('k'):
                promotion_piece = Knight(self.ending_square, self.player)
            elif promotion_piece_code in ('b'):
                promotion_piece = Bishop(self.ending_square, self.player)
            elif promotion_piece_code in ('r'):
                promotion_piece = Rook(self.ending_square, self.player)

            new_board.dict_of_64_squares[self.ending_square.get_square_index_string()].current_occupant = promotion_piece

        else:
            new_board.dict_of_64_squares[self.ending_square.get_square_index_string()].current_occupant = self.starting_square.current_occupant

        # Set the updated board as the ending_board.
        self.ending_board = new_board



    def set_captured_piece(self):
        if self.ending_square.current_occupant is not None and self.ending_square.current_occupant.owner.color != self.player.color:
            self.captured_piece = self.ending_square.current_occupant



    def set_is_check(self):
        self.is_check = not(self.ending_board.is_king_not_in_check(self.player.get_opponents_color_index()))



    def set_is_promotion(self):
        if isinstance(self.starting_square.current_occupant, Pawn):
            if self.ending_square.number_index == 1 and self.player.color == 0:    # Black pawn
                self.is_promotion = True
            elif self.ending_square.number_index == 8 and self.player.color == 1:    # White pawn
                self.is_promotion = True





    def set_ordinal_number(self, list_of_confirmed_turns):
        if len(list_of_confirmed_turns) == 0:
            # This is the first white turn.
            current_ordinal = 1
        elif len(list_of_confirmed_turns) == 1:
            # This is the first black turn.
            current_ordinal = 1
        else:
            # Both players have taken at least one turn.
            last_turn_ordinal = list_of_confirmed_turns[-1].ordinal_number
            two_turns_ago_ordinal = list_of_confirmed_turns[-2].ordinal_number

            if last_turn_ordinal == two_turns_ago_ordinal:
                # It's white's turn, so ordinal should increment by 1.
                current_ordinal = last_turn_ordinal + 1
            else:
                # It's black's turn, so ordinal should be the same as last turn.
                current_ordinal = last_turn_ordinal

        self.ordinal_number = current_ordinal



    def set_is_checkmate(self):
        pass    #TODO




    def set_notation(self):
        pass    #TODO



class Piece(object):


    def __init__(self, current_square, owner, unicode_characters, has_moved_previously=False):
        self.current_square = current_square
        self.owner = owner  # Should be a Player object.
        self.unicode = unicode_characters[self.owner.color]     # Since Black = 0 and White = 1, can index the list using color value.
        self.has_moved_previously = has_moved_previously

        self.turn_captured = None



    def path_to_target_is_unblocked(self, target_square, board):
        # INPUT VALIDATION TYPE 5: Check to see if any square along the path is occupied.

        ###print("Begin check 5...")
        from Services import produce_path_between_two_squares
        path = produce_path_between_two_squares(self.current_square, target_square, board)
        ###print("Length of path: ", len(path))
        if len(path) == 0:
            # There is no path, and so nothing is blocked.
            pass
        else:
            # There is a path, so need to check each square in the path.
            for square in path:
                ###print("Square in path: ", square.get_square_index_string())
                if square.current_occupant is not None:
                    ###print("This square is blocking the path - FAILED check 5")
                    return False
                ###else:
                    ###print("This square is clear.")
        ###print("Passed check 5")
        return True



class Pawn(Piece):

    def __init__(self, current_square, owner, has_moved_previously=False):
        unicode_characters = ["♙", "♟"]
        super().__init__(current_square, owner, unicode_characters, has_moved_previously)

        self.points = 1



    def target_can_be_reached(self, target_square):
        # INPUT VALIDATION TYPE 4: Check to see if the target square can be reached, assuming an empty board.

        x1 = self.current_square.letter_index
        y1 = self.current_square.number_index
        x2 = target_square.letter_index
        y2 = target_square.number_index

        if self.owner.color == 1:
            # White pawns
            if x1 == x2 and y2 == y1 + 1 and target_square.current_occupant is None:
                valid = True
            elif x1 == x2 and y2 == y1 + 2 and self.has_moved_previously is False and target_square.current_occupant is None:
                valid = True
            elif abs(x2 - x1) == 1 and y2 == y1 + 1 and target_square.current_occupant is not None and target_square.current_occupant.owner.color == 0:
                valid = True
            else:
                valid = False
        elif self.owner.color == 0:
            # Black pawns
            if x1 == x2 and y2 == y1 - 1 and target_square.current_occupant is None:
                valid = True
            elif x1 == x2 and y2 == y1 - 2 and self.has_moved_previously is False and target_square.current_occupant is None:
                valid = True
            elif abs(x2 - x1) == 1 and y2 == y1 - 1 and target_square.current_occupant is not None and target_square.current_occupant.owner.color == 1:
                valid = True
            else:
                valid = False
        else:
            # Throw error
            raise Exception("This is an error!")

        ###if valid is True:
            ###print("Pawn passed check 4")
        return valid



class Rook(Piece):

    def __init__(self, current_square, owner, has_moved_previously=False):
        unicode_characters = ["♖", "♜"]
        super().__init__(current_square, owner, unicode_characters, has_moved_previously)

        self.points = 5



    def target_can_be_reached(self, target_square):
        # INPUT VALIDATION TYPE 4: Check to see if the target square can be reached, assuming an empty board.

        x1 = self.current_square.letter_index
        y1 = self.current_square.number_index
        x2 = target_square.letter_index
        y2 = target_square.number_index


        if x1 == x2 or y1 == y2:
            ###print("Rook passed check 4")
            return True
        else:
            return False



class Knight(Piece):

    def __init__(self, current_square, owner, has_moved_previously=False):
        unicode_characters = ["♘", "♞"]
        super().__init__(current_square, owner, unicode_characters, has_moved_previously)

        self.points = 3

        

    def target_can_be_reached(self, target_square):
        # INPUT VALIDATION TYPE 4: Check to see if the target square can be reached, assuming an empty board.

        # Need to confirm that target_square is an L-shaped jump away from the current_square.
        x1 = self.current_square.letter_index
        y1 = self.current_square.number_index
        x2 = target_square.letter_index
        y2 = target_square.number_index

        if abs(x2 - x1) <= 2 and abs(y2 - y1) <= 2 and abs(x2 - x1) + abs(y2 - y1) == 3:
            ###print("Knight passed check 4")
            return True
        else:
            return False
        


    def path_to_target_is_unblocked(self, target_square, board):
        # Used for INPUT VALIDATION TYPE 5
        # The knight's path is never blocked because it leaps over other pieces.
        ###print("Knight passed check 5")
        return True



class Bishop(Piece):

    def __init__(self, current_square, owner, has_moved_previously=False):
        unicode_characters = ["♗", "♝"]
        super().__init__(current_square, owner, unicode_characters, has_moved_previously)

        self.points = 3


    def target_can_be_reached(self, target_square):
        # INPUT VALIDATION TYPE 4: Check to see if the target square can be reached, assuming an empty board.

        x1 = self.current_square.letter_index
        y1 = self.current_square.number_index
        x2 = target_square.letter_index
        y2 = target_square.number_index

        if abs(x1 - x2) == abs(y1 - y2):
            ###print("Bishop passed check 4")
            return True
        else:
            return False



class Queen(Piece):

    def __init__(self, current_square, owner, has_moved_previously=False):
        unicode_characters = ["♕", "♛"]
        super().__init__(current_square, owner, unicode_characters, has_moved_previously)

        self.points = 9


    def target_can_be_reached(self, target_square):
        # INPUT VALIDATION TYPE 4: Check to see if the target square can be reached, assuming an empty board.

        x1 = self.current_square.letter_index
        y1 = self.current_square.number_index
        x2 = target_square.letter_index
        y2 = target_square.number_index

        if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            ###print("Queen passed check 4")
            return True
        else:
            return False



class King(Piece):

    def __init__(self, current_square, owner, has_moved_previously=False):
        unicode_characters = ["♔", "♚"]
        super().__init__(current_square, owner, unicode_characters, has_moved_previously)


    def target_can_be_reached(self, target_square):
        # INPUT VALIDATION TYPE 4: Check to see if the target square can be reached, assuming an empty board.

        # Need to confirm that target_square is one square away from the current_square.
        x1 = self.current_square.letter_index
        y1 = self.current_square.number_index
        x2 = target_square.letter_index
        y2 = target_square.number_index

        if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 and abs(x1 - x2) + abs(y1 - y2) > 0:
            ###print("King passed check 4")
            return True
        else:
            return False



    def path_to_target_is_unblocked(self, target_square, board):
        # Used for INPUT VALIDATION TYPE 5
        # The king's path is never blocked because he can only move one square.
        ###print("King passed check 5")
        return True


