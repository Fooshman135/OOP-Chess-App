# Tests

# HOW TO RUN THESE TESTS:
#
# 1) Install the pytest module using Pip (if not already installed).
# 2) Run the following command at the Terminal prompt (not the Python prompt):
#       pytest Tests.py
#

import pytest
from Services import letter_index_to_letter
from Services import square_indices_to_string
from Services import color_number_to_text
from Services import produce_path_between_two_squares


class TestLetterIndexToLetter:

	def test_works(self):
		# Returns expected value ("e") when passed 5.
		# Note that this test is unnecessary due to the below parametrized test.

		result = letter_index_to_letter(5)
		assert result == "e", "Expected letter to match but it did not."


	@pytest.mark.parametrize("test_input,expected",[
		(1, "a"),
		(2, "b"),
		(3, "c"),
		(4, "d"),
		(5, "e"),
		(6, "f"),
		(7, "g"),
		(8, "h"),
	])
	def test_works_for_expected_input(self, test_input, expected):
		# Returns expected value when passed valid input.
		result = letter_index_to_letter(test_input)
		assert result == expected, "Expected letter to match but it did not."


	@pytest.mark.parametrize("test_input",[
		None,
		-7,
		50,
		"foobar",
	])
	def test_fails_for_invalid_input(self, test_input):
		# Raises an exception when bad input is passed in.
		with pytest.raises(Exception):
			letter_index_to_letter(test_input)



class TestSquareIndicesToString:

	@pytest.mark.parametrize("test_input_1,test_input_2,expected",[
		(1,1, "a1"),
		(1,8, "a8"),
		(8,1, "h1"),
		(8,8, "h8"),
	])
	def test_works_for_expected_input(self, test_input_1, test_input_2, expected):
		# Returns expected value when passed valid input.
		result = square_indices_to_string(test_input_1,test_input_2)
		assert result == expected, "Expected square index string to match but it did not."



class TestColorNumberToText:

	@pytest.mark.parametrize("test_input,expected",[
		(0, "Black"),
		(1, "White"),
	])
	def test_works_for_expected_input(self, test_input, expected):
		# Returns expected value when passed valid input.
		result = color_number_to_text(test_input)
		assert result == expected, "Expected color string to match color index but it did not."


	@pytest.mark.parametrize("test_input",[
		None,
		-1,
		2,
		"foobar",
	])
	def test_fails_for_invalid_input(self, test_input):
		# Raises an exception when bad input is passed in.
		with pytest.raises(Exception):
			color_number_to_text(test_input)



class TestProducePathBetweenTwoSquares:

	from Model import Board
	test_board = Board()

	a1 = test_board.dict_of_64_squares["a1"]
	f1 = test_board.dict_of_64_squares["f1"]
	d4 = test_board.dict_of_64_squares["d4"]
	b6 = test_board.dict_of_64_squares["b6"]
	b7 = test_board.dict_of_64_squares["b7"]

	test_path_one = [
		test_board.dict_of_64_squares["b1"],
		test_board.dict_of_64_squares["c1"],
		test_board.dict_of_64_squares["d1"],
		test_board.dict_of_64_squares["e1"],
	]

	test_path_two = [
		test_board.dict_of_64_squares["b2"],
		test_board.dict_of_64_squares["c3"],
	]

	test_path_three = [
		test_board.dict_of_64_squares["c5"],
	]

	test_path_four = []


	@pytest.mark.parametrize("test_input_1, test_input_2, test_input_3, expected",[
		(a1, f1, test_board, test_path_one),
		(a1, d4, test_board, test_path_two),
		(d4, b6, test_board, test_path_three),
		(b6, b7, test_board, test_path_four),
		(a1, b6, test_board, test_path_four),
	])
	def test_works_for_expected_input(self, test_input_1, test_input_2, test_input_3, expected):
		# Returns expected value when passed valid input.
		result = produce_path_between_two_squares(test_input_1, test_input_2, test_input_3)
		assert set(result) == set(expected), "Expected path to match expected set of Squares but it did not."
