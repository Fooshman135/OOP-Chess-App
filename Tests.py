# Tests

from Model import *
from Services import *






# Unit tests for the King's is_move_legal method.


# Unit test #1: King in center of empty board.

# First, generate empty board.
# Second, initialize King on square e5.
# Third, run the method using d4 as the target_square.
# Fourth, confirm that output is TRUE.




#############################


# Unit tests for the get_square_from_indexes function.
# Assumes that the generate_empty_board() function works perfectly.


# Unit test #1: Given empty board, return square a1.


my_empty_board = generate_empty_board()

my_square = get_square_from_indexes(my_empty_board,1,1)

print(type(my_square))
print(my_square.letter_index)
print(my_square.number_index)

