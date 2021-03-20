# Controller

from Model import *


# Create a Game object.
my_game = Game()


# Begin game cycle.
while True:
    my_game.game_loop()

    if my_game.checkmate_achieved is True:
        break


# The game is over because one player checkmated the other.

print("\n\nGAME OVER! {} WON!".format(color_number_to_text(my_game.whose_turn.get_opponents_color_index())))


