# Controller

from Model import *
from Services import *
from View import *



# First, create the two players.
white_player = Player(1)
black_player = Player(0)


# Then, create a new board.
my_board = Board(is_current=1, whose_turn=white_player)


# Next, add the pieces to the starting positions on the board.
pieces_into_starting_positions(dict_of_squares, white_player, black_player)


# Next, create a Game object.
my_game = Game(white_player, black_player, current_board = my_board)


# Delete unused objects, now that their data is saved within the Game object.
del white_player
del black_player
del my_board



# Begin game cycle.
while True:
  game_loop(my_game)




