# Controller

from Model import *


# Create a Game object.
my_game = Game()


# Begin game cycle.
while True:
    my_game.game_loop()

    if my_game.checkmate_achieved is True or my_game.stalemate_achieved is True:
        break


# The game is over because one player checkmated the other or stalemate was reached.

declare_game_over(my_game)

