# Controller

from Model import *
from Services import *
from View import *



# Generate the empty board by instantiating 64 Square objects.


list_of_squares = []

color = 1

# In the following nested for loops, "i" is the letter_index and "j" is the number_index.

for i in range(1,9):
    color += 1      # Flip the square color back (every time we increment the row).
    for j in range(1,9):
        list_of_squares.append(Square(i, j, color_number_to_text(color % 2)))
        color += 1      # Flip the square color

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



# Now let's test the get_square_from_indexes function:

meow = get_square_from_indexes(list_of_squares,1,1)

print(type(meow))
print(meow.letter_index)
print(meow.number_index)




# Now print the board

# View.print_current_board_cli()

 

