# Services

from Model import *




def color_number_to_text(num):

	# Black = 0, White = 1

	if num % 2 == 0:
		text = "Black"
	else:
		text = "White"

	return text



def get_square_from_indexes(array_of_squares,letter_index_here, number_index_here):
	x = None

	for i in range(len(array_of_squares)):
		if (array_of_squares[i].letter_index == letter_index_here and array_of_squares[i].number_index == number_index_here):
			x = array_of_squares[i]
			break


	if x is None:
		# Throw error
		raise Exception("This is an error!")


	return x




def generate_empty_board():

	# Generate the empty board by instantiating 64 Square objects.

	list_of_squares = []

	color = 1

	# In the following nested for loops, "i" is the letter_index and "j" is the number_index.

	for i in range(1,9):
	    color += 1      # Flip the square color back (every time we increment the row).
	    for j in range(1,9):
	        list_of_squares.append(Square(i, j, color_number_to_text(color % 2)))
	        color += 1      # Flip the square color

	return list_of_squares


	       #  # Now place the pieces in their starting positions on the board.
	       #  if j == 2:
	       #      list_of_squares[-1].occupant_type = Pawn()
	       #      list_of_squares[-1].occupant_color = color_number_to_text(1)
	       #  if j == 7:
	       #      list_of_squares[-1].occupant_type = Pawn()
	       #      list_of_squares[-1].occupant_color = color_number_to_text(0)



	       #  # For testing purposes, show the properties of the current square.
	       # print(list_of_squares[-1].letter_index)
	       # print(list_of_squares[-1].number_index)
	       #  print(list_of_squares[-1].square_color)
	       #  # print(list_of_squares[-1].occupant_type)
	       # #  print(list_of_squares[-1].occupant_color)
	       #  print("")






def pieces_into_starting_positions(board):
	# board is a list of Square objects.
	# This function assigns a piece to each Square as the starting position.
	pass



