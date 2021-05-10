# Tests

# HOW TO RUN THESE TESTS:
#
# 1) Install the pytest module using Pip (if not already installed).
# 2) Run the following command at the Terminal prompt (not the Python prompt):
#       pytest Tests.py
#

import pytest
from Services import letter_index_to_letter
from Services import color_number_to_text


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



class TestColorNumberToText:

	@pytest.mark.parametrize("test_input,expected",[
		(0, "Black"),
		(1, "White"),
	])
	def test_works_for_expected_input(self, test_input, expected):
		# Returns expected value when passed valid input.
		result = color_number_to_text(test_input)
		assert result == expected, "Expected letter to match but it did not."


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


