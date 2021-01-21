# Services


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


	if x is None:
		# Throw error
		raise Exception("This is an error!")


	return x



def pieces_into_starting_positions(board):
	# board is a list of Square objects.
	# This function assigns a piece to each Square as the starting position.
	pass



