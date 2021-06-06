# Tests

# HOW TO RUN THESE TESTS:
#
# 1) Install the pytest module using Pip (if not already installed).
# 2) Run the following command at the Terminal prompt (not the Python prompt) at the app's root directory:
#       pytest


import pytest
from Model import Turn, Board, Player, Rook, Knight, Bishop, Queen, King, Pawn



class TestIsLegalMoveCastling:


	white_player = Player(1)
	black_player = Player(0)

	board_one = Board()
	board_one.pieces_into_specified_positions({
		"a1": Rook(None, white_player),
		"b1": Knight(None, white_player),
		"c1": Bishop(None, white_player),
		"d1": Queen(None, white_player),
		"e1": King(None, white_player),
		"c4": Bishop(None, white_player),
		"f3": Knight(None, white_player),
		"h1": Rook(None, white_player),

		"a2": Pawn(None, white_player),
		"b2": Pawn(None, white_player),
		"c2": Pawn(None, white_player),
		"d2": Pawn(None, white_player),
		"e4": Pawn(None, white_player),
		"f2": Pawn(None, white_player),
		"g2": Pawn(None, white_player),
		"h2": Pawn(None, white_player),

		"a7": Pawn(None, black_player),
		"b7": Pawn(None, black_player),
		"c7": Pawn(None, black_player),
		"d6": Pawn(None, black_player),
		"e5": Pawn(None, black_player),
		"f7": Pawn(None, black_player),
		"g7": Pawn(None, black_player),
		"h7": Pawn(None, black_player),

		"a8": Rook(None, black_player),
		"b8": Knight(None, black_player),
		"g4": Bishop(None, black_player),
		"d8": Queen(None, black_player),
		"e8": King(None, black_player),
		"f8": Bishop(None, black_player),
		"g8": Knight(None, black_player),
		"h8": Rook(None, black_player),
	})
	board_two = Board()
	board_two.pieces_into_specified_positions({
		"a1": Rook(None, white_player),
		"b1": Knight(None, white_player),
		"c1": Bishop(None, white_player),
		"d1": Queen(None, white_player),
		"e1": King(None, white_player, True),
		"c4": Bishop(None, white_player),
		"f3": Knight(None, white_player),
		"h1": Rook(None, white_player),

		"a2": Pawn(None, white_player),
		"b2": Pawn(None, white_player),
		"c2": Pawn(None, white_player),
		"d2": Pawn(None, white_player),
		"e4": Pawn(None, white_player),
		"f2": Pawn(None, white_player),
		"g2": Pawn(None, white_player),
		"h2": Pawn(None, white_player),

		"a7": Pawn(None, black_player),
		"b7": Pawn(None, black_player),
		"c7": Pawn(None, black_player),
		"d6": Pawn(None, black_player),
		"e5": Pawn(None, black_player),
		"f7": Pawn(None, black_player),
		"g7": Pawn(None, black_player),
		"h7": Pawn(None, black_player),

		"a8": Rook(None, black_player),
		"b8": Knight(None, black_player),
		"g4": Bishop(None, black_player),
		"d8": Queen(None, black_player),
		"e8": King(None, black_player),
		"f8": Bishop(None, black_player),
		"g8": Knight(None, black_player),
		"h8": Rook(None, black_player),
	})
	board_three = Board()
	board_three.pieces_into_specified_positions({
		"a1": Rook(None, white_player),
		"b1": Knight(None, white_player),
		"c1": Bishop(None, white_player),
		"d1": Queen(None, white_player),
		"e1": King(None, white_player),
		"c4": Bishop(None, white_player),
		"f3": Knight(None, white_player),
		"h1": Rook(None, white_player, True),

		"a2": Pawn(None, white_player),
		"b2": Pawn(None, white_player),
		"c2": Pawn(None, white_player),
		"d2": Pawn(None, white_player),
		"e4": Pawn(None, white_player),
		"f2": Pawn(None, white_player),
		"g2": Pawn(None, white_player),
		"h2": Pawn(None, white_player),

		"a7": Pawn(None, black_player),
		"b7": Pawn(None, black_player),
		"c7": Pawn(None, black_player),
		"d6": Pawn(None, black_player),
		"e5": Pawn(None, black_player),
		"f7": Pawn(None, black_player),
		"g7": Pawn(None, black_player),
		"h7": Pawn(None, black_player),

		"a8": Rook(None, black_player),
		"b8": Knight(None, black_player),
		"g4": Bishop(None, black_player),
		"d8": Queen(None, black_player),
		"e8": King(None, black_player),
		"f8": Bishop(None, black_player),
		"g8": Knight(None, black_player),
		"h8": Rook(None, black_player),
	})
	board_four = Board()
	board_four.pieces_into_specified_positions({
		"a1": Rook(None, white_player),
		"b1": Knight(None, white_player),
		"c1": Bishop(None, white_player),
		"d1": Queen(None, white_player),
		"e1": King(None, white_player),
		"f3": Knight(None, white_player),
		"h1": Rook(None, white_player),

		"a2": Pawn(None, white_player),
		"b2": Pawn(None, white_player),
		"c2": Pawn(None, white_player),
		"d2": Pawn(None, white_player),
		"e4": Pawn(None, white_player),
		"f2": Pawn(None, white_player),
		"g2": Pawn(None, white_player),
		"h2": Pawn(None, white_player),

		"a7": Pawn(None, black_player),
		"b6": Pawn(None, black_player),
		"c7": Pawn(None, black_player),
		"d7": Pawn(None, black_player),
		"e5": Pawn(None, black_player),
		"f7": Pawn(None, black_player),
		"g7": Pawn(None, black_player),
		"h7": Pawn(None, black_player),

		"a8": Rook(None, black_player),
		"b8": Knight(None, black_player),
		"a6": Bishop(None, black_player),
		"d8": Queen(None, black_player),
		"e8": King(None, black_player),
		"f8": Bishop(None, black_player),
		"g8": Knight(None, black_player),
		"h8": Rook(None, black_player),
	})
	board_five = Board()
	board_five.pieces_into_specified_positions({
		"a1": Rook(None, white_player),
		"b1": Knight(None, white_player),
		"c1": Bishop(None, white_player),
		"d1": Queen(None, white_player),
		"e1": King(None, white_player),
		"f3": Knight(None, white_player),
		"h1": Rook(None, white_player),

		"a2": Pawn(None, white_player),
		"b2": Pawn(None, white_player),
		"c2": Pawn(None, white_player),
		"d2": Pawn(None, white_player),
		"e4": Pawn(None, white_player),
		"f2": Pawn(None, white_player),
		"g2": Pawn(None, white_player),
		"h2": Pawn(None, white_player),

		"a7": Pawn(None, black_player),
		"b6": Pawn(None, black_player),
		"c7": Pawn(None, black_player),
		"d7": Pawn(None, black_player),
		"e5": Pawn(None, black_player),
		"f7": Pawn(None, black_player),
		"g7": Pawn(None, black_player),
		"h7": Pawn(None, black_player),

		"a8": Rook(None, black_player),
		"b8": Knight(None, black_player),
		"f1": Bishop(None, black_player),
		"d8": Queen(None, black_player),
		"e8": King(None, black_player),
		"f8": Bishop(None, black_player),
		"g8": Knight(None, black_player),
		"h8": Rook(None, black_player),
	})
	board_six = Board()
	board_six.pieces_into_specified_positions({
		"a1": Rook(None, white_player),
		"b1": Knight(None, white_player),
		"c1": Bishop(None, white_player),
		"d1": Queen(None, white_player),
		"e1": King(None, white_player),
		"f1": Bishop(None, white_player),
		"f3": Knight(None, white_player),
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
	})
	board_seven = Board()
	board_seven.pieces_into_specified_positions({
		"a1": Rook(None, white_player),
		"a3": Knight(None, white_player),
		"e3": Bishop(None, white_player),
		"d3": Queen(None, white_player),
		"e1": King(None, white_player),
		"f1": Bishop(None, white_player),
		"f3": Knight(None, white_player),
		"h1": Rook(None, white_player),

		"a2": Pawn(None, white_player),
		"b2": Pawn(None, white_player),
		"c2": Pawn(None, white_player),
		"d4": Pawn(None, white_player),
		"e2": Pawn(None, white_player),
		"f2": Pawn(None, white_player),
		"g2": Pawn(None, white_player),
		"h2": Pawn(None, white_player),

		"a7": Pawn(None, black_player),
		"b7": Pawn(None, black_player),
		"c6": Pawn(None, black_player),
		"d5": Pawn(None, black_player),
		"e6": Pawn(None, black_player),
		"f7": Pawn(None, black_player),
		"g7": Pawn(None, black_player),
		"h7": Pawn(None, black_player),

		"a8": Rook(None, black_player),
		"b8": Knight(None, black_player),
		"c8": Bishop(None, black_player),
		"a5": Queen(None, black_player),
		"e8": King(None, black_player),
		"f8": Bishop(None, black_player),
		"g8": Knight(None, black_player),
		"h8": Rook(None, black_player),
	})
	board_eight = Board()
	board_eight.pieces_into_specified_positions({
		"a1": Rook(None, white_player),
		"e3": Bishop(None, white_player),
		"d2": Queen(None, white_player),
		"e1": King(None, white_player),
		"f1": Bishop(None, white_player),
		"f3": Knight(None, white_player),
		"h1": Rook(None, white_player),

		"a2": Pawn(None, white_player),
		"b2": Pawn(None, white_player),
		"d4": Pawn(None, white_player),
		"e2": Pawn(None, white_player),
		"f2": Pawn(None, white_player),
		"g2": Pawn(None, white_player),
		"h2": Pawn(None, white_player),

		"a7": Pawn(None, black_player),
		"b7": Pawn(None, black_player),
		"c7": Pawn(None, black_player),
		"d6": Pawn(None, black_player),
		"e7": Pawn(None, black_player),
		"f7": Pawn(None, black_player),
		"g7": Pawn(None, black_player),
		"h7": Pawn(None, black_player),

		"a8": Rook(None, black_player),
		"b8": Knight(None, black_player),
		"b1": Bishop(None, black_player),
		"d8": Queen(None, black_player),
		"e8": King(None, black_player),
		"f8": Bishop(None, black_player),
		"g8": Knight(None, black_player),
		"h8": Rook(None, black_player),
	})

	turn_one = Turn(
		starting_board = board_one, 
		player = white_player, 
		starting_square = board_one.dict_of_64_squares["e1"], 
		ending_square = board_one.dict_of_64_squares["g1"]
	)
	turn_two = Turn(
		starting_board = board_one, 
		player = white_player, 
		starting_square = board_one.dict_of_64_squares["h1"], 
		ending_square = board_one.dict_of_64_squares["f1"]
	)
	turn_three = Turn(
		starting_board = board_one, 
		player = white_player, 
		starting_square = board_one.dict_of_64_squares["e1"], 
		ending_square = board_one.dict_of_64_squares["f1"]
	)
	turn_four = Turn(
		starting_board = board_one, 
		player = white_player, 
		starting_square = board_one.dict_of_64_squares["e1"], 
		ending_square = board_one.dict_of_64_squares["e2"]
	)
	turn_five = Turn(
		starting_board = board_two, 
		player = white_player, 
		starting_square = board_two.dict_of_64_squares["e1"], 
		ending_square = board_two.dict_of_64_squares["g1"]
	)
	turn_six = Turn(
		starting_board = board_three, 
		player = white_player, 
		starting_square = board_three.dict_of_64_squares["e1"], 
		ending_square = board_three.dict_of_64_squares["g1"]
	)
	turn_seven = Turn(
		starting_board = board_four, 
		player = white_player, 
		starting_square = board_four.dict_of_64_squares["e1"], 
		ending_square = board_four.dict_of_64_squares["g1"]
	)
	turn_eight = Turn(
		starting_board = board_five, 
		player = white_player, 
		starting_square = board_five.dict_of_64_squares["e1"], 
		ending_square = board_five.dict_of_64_squares["g1"]
	)
	turn_nine = Turn(
		starting_board = board_six, 
		player = white_player, 
		starting_square = board_six.dict_of_64_squares["e1"], 
		ending_square = board_six.dict_of_64_squares["g1"]
	)
	turn_ten = Turn(
		starting_board = board_seven, 
		player = white_player, 
		starting_square = board_seven.dict_of_64_squares["e1"], 
		ending_square = board_seven.dict_of_64_squares["g1"]
	)
	turn_eleven = Turn(
		starting_board = board_eight, 
		player = white_player, 
		starting_square = board_eight.dict_of_64_squares["e1"], 
		ending_square = board_eight.dict_of_64_squares["g1"]
	)


	@pytest.mark.parametrize("test_input, expected",[
		(turn_one, True),			# No complications
		(turn_two, False),			# Rook selected to move instead of King
		(turn_three, False),		# King moved one space over instead of two
		(turn_four, False),			# King moved to different row
		(turn_five, False),			# King was moved in a previous turn
		(turn_six, False),			# Rook was moved in a previous turn
		(turn_seven, False),		# King passes through check while castling
		(turn_eight, False),		# King's path is blocked by enemy piece
		(turn_nine, False),			# King's path is blocked by own piece
		(turn_ten, False),			# King starts off in check
		(turn_eleven, False),		# Rook's path is blocked by enemy piece

	])
	def test_works_for_expected_input(self, test_input, expected):
		# Returns expected value when passed valid input.
		result = test_input.is_legal_move_castling()
		assert result == expected, "Expected Turn to identify legal castling move."



