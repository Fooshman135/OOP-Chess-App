# Tests

from Model import *
from Services import *


#############################


# Unit tests for the King's is_move_legal method.


# Unit test #1: King in center of empty board.

# First, generate empty board.
# Second, initialize King on square e5.
# Third, run the method using d4 as the target_square.
# Fourth, confirm that output is TRUE.




#############################


# Unit tests for the get_square_from_indexes function.
# Assumes that the generate_empty_board() function works perfectly.
# Assumes that the letter_index_to_letter() function works perfectly.


def unit_test_for__get_square_from_indexes():


	print("Unit test #1: Given empty board, return square a1.\n")

	my_empty_board = generate_empty_board()
	my_square = get_square_from_indexes(my_empty_board,1,1)

	print("The type of object returned is: ", type(my_square))
	print("The returned square is: ", letter_index_to_letter(my_square.letter_index), my_square.number_index, sep='')


	print("\n------------")
	print("Unit test #2: Given empty board, try to return square a9 but throw error instead.\n")

	my_empty_board = generate_empty_board()

	try:
		my_square = get_square_from_indexes(my_empty_board,1,9)
	except:
		print("It successfully threw an error!")





#############################


# Unit tests for letter_index_to_letter() function.

def unit_test_for__letter_index_to_letter():


	print("Unit test #1: Given number 5, return 'e'.\n")

	my_letter = letter_index_to_letter(5)
	print("The returned letter is:", my_letter)


	print("\n------------")
	print("Unit test #2: Given number 9, throw exception.\n")

	try:
		my_letter = letter_index_to_letter(9)
	except:
		print("It successfully threw an error!")




#############################


# Here's where I can run the tests (uncomment whichever test I want to run):



# unit_test_for__get_square_from_indexes()

#unit_test_for__letter_index_to_letter()






#############################



