# View

from Model import *



def print_current_board_cli():

    # board is a dictionary of 64 square objects.

    # ♟♙♞♘♝♗♛♕♚♔♜♖



    # title =       "     a   b   c   d   e   f   g   h   "
    # title_line =  "    _________________________________"
    # row_8 =       "8   |   |   |   |   |   |   |   |   |"
    # row_8_line =  "    _________________________________"
    # row_7 =       "7   |   |   |   |   |   |   |   |   |"
    # row_7_line =  "    _________________________________"
    # row_6 =       "6   |   |   |   |   |   |   |   |   |"
    # row_6_line =  "    _________________________________"
    # row_5 =       "5   |   |   |   |   |   |   |   |   |"
    # row_5_line =  "    _________________________________"
    # row_4 =       "4   |   |   |   |   |   |   |   |   |"
    # row_4_line =  "    _________________________________"
    # row_3 =       "3   |   |   |   |   |   |   |   |   |"
    # row_3_line =  "    _________________________________"
    # row_2 =       "2   |   |   |   |   |   |   |   |   |"
    # row_2_line =  "    _________________________________"   
    # row_1 =       "1   |   |   |   |   |   |   |   |   |"
    # row_1_line =  "    _________________________________"



    title =       "     a     b   c   d   e   f   g   h "
    title_line =  "    _________________________________"
    row_8 =       "8   | {a8} | {b8} | {c8} | {d8} | {e8} | {f8} | {g8} | {h8} |".format(a8 = "♖", b8 = "♘", c8 = "♗", d8 = "♕", e8 = "♔", f8 = "♗", g8 = "♘", h8 = "♖")
    row_8_line =  "    _________________________________"
    row_7 =       "7   | {a7} | {b7} | {c7} | {d7} | {e7} | {f7} | {g7} | {h7} |".format(a7 = "♙", b7 = "♙", c7 = "♙", d7 = "♙", e7 = "♙", f7 = "♙", g7 = "♙", h7 = "♙")
    row_7_line =  "    _________________________________"
    row_6 =       "6   |   |   |   |   |   |   |   |   |"
    row_6_line =  "    _________________________________"
    row_5 =       "5   |   |   |   |   |   |   |   |   |"
    row_5_line =  "    _________________________________"
    row_4 =       "4   |   |   |   |   |   |   |   |   |"
    row_4_line =  "    _________________________________"
    row_3 =       "3   |   |   |   |   |   |   |   |   |"
    row_3_line =  "    _________________________________"
    row_2 =       "2   |   |   |   |   |   |   |   |   |"
    row_2_line =  "    _________________________________"   
    row_1 =       "1   |   |   |   |   |   |   |   |   |"
    row_1_line =  "    _________________________________"




    print(title)
    print(title_line)
    print(row_8)
    print(row_8_line)
    print(row_7)
    print(row_7_line)
    print(row_6)
    print(row_6_line)
    print(row_5)
    print(row_5_line)
    print(row_4)
    print(row_4_line)
    print(row_3)
    print(row_3_line)
    print(row_2)
    print(row_2_line)
    print(row_1)
    print(row_1_line)





print_current_board_cli()