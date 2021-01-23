# Controller

from Model import *
from Services import *
from View import *



# First, create a new board.
board = generate_empty_board()


# Next, add the pieces to the starting positions on the board.
pieces_into_starting_positions(board)


# Now print the board
print_board_white_bottom_cli(board)

 

