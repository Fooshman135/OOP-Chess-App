# Controller

from Model import *
from Services import *
from View import *



# First, create the two players.
white_player = Player(1)
black_player = Player(0)


# Then, create a new board.
dict_of_squares = generate_empty_board()


# Next, add the pieces to the starting positions on the board.
pieces_into_starting_positions(dict_of_squares, white_player, black_player)


# Now instantiate a Board object.
my_board = Board(dict_of_64_squares = dict_of_squares, is_current=1, whose_turn=1)



# Next, create a Game object.
my_game = Game(white_player, black_player, current_board = my_board)




# Now print the board.
print_board_white_bottom_cli(my_game.current_board)

 

