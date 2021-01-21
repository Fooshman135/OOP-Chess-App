# View

from Model import *



def print_current_board_white_bottom_cli(board):

    # board is a dictionary of 64 square objects.

    # The following dictionary comprehension assigns a space to empty squares, and assigns the piece's unicode to occupied squares.
    unicode_dict = {k: (" " if v.current_occupant == None else v.current_occupant.unicode) for (k,v) in board.items()}


    # Now produce the strings used to show the board.
    title =       "      a   b   c   d   e   f   g   h "
    title_line =  "    _________________________________"
    row_8 =       "8   | {a8} | {b8} | {c8} | {d8} | {e8} | {f8} | {g8} | {h8} |".format(a8 = unicode_dict["a8"], b8 = unicode_dict["b8"], c8 = unicode_dict["c8"], d8 = unicode_dict["d8"], e8 = unicode_dict["e8"], f8 = unicode_dict["f8"], g8 = unicode_dict["g8"], h8 = unicode_dict["h8"])
    row_8_line =  "    _________________________________"
    row_7 =       "7   | {a7} | {b7} | {c7} | {d7} | {e7} | {f7} | {g7} | {h7} |".format(a7 = unicode_dict["a7"], b7 = unicode_dict["b7"], c7 = unicode_dict["c7"], d7 = unicode_dict["d7"], e7 = unicode_dict["e7"], f7 = unicode_dict["f7"], g7 = unicode_dict["g7"], h7 = unicode_dict["h7"])
    row_7_line =  "    _________________________________"
    row_6 =       "6   | {a6} | {b6} | {c6} | {d6} | {e6} | {f6} | {g6} | {h6} |".format(a6 = unicode_dict["a6"], b6 = unicode_dict["b6"], c6 = unicode_dict["c6"], d6 = unicode_dict["d6"], e6 = unicode_dict["e6"], f6 = unicode_dict["f6"], g6 = unicode_dict["g6"], h6 = unicode_dict["h6"])
    row_6_line =  "    _________________________________"
    row_5 =       "5   | {a5} | {b5} | {c5} | {d5} | {e5} | {f5} | {g5} | {h5} |".format(a5 = unicode_dict["a5"], b5 = unicode_dict["b5"], c5 = unicode_dict["c5"], d5 = unicode_dict["d5"], e5 = unicode_dict["e5"], f5 = unicode_dict["f5"], g5 = unicode_dict["g5"], h5 = unicode_dict["h5"])
    row_5_line =  "    _________________________________"
    row_4 =       "4   | {a4} | {b4} | {c4} | {d4} | {e4} | {f4} | {g4} | {h4} |".format(a4 = unicode_dict["a4"], b4 = unicode_dict["b4"], c4 = unicode_dict["c4"], d4 = unicode_dict["d4"], e4 = unicode_dict["e4"], f4 = unicode_dict["f4"], g4 = unicode_dict["g4"], h4 = unicode_dict["h4"])
    row_4_line =  "    _________________________________"
    row_3 =       "3   | {a3} | {b3} | {c3} | {d3} | {e3} | {f3} | {g3} | {h3} |".format(a3 = unicode_dict["a3"], b3 = unicode_dict["b3"], c3 = unicode_dict["c3"], d3 = unicode_dict["d3"], e3 = unicode_dict["e3"], f3 = unicode_dict["f3"], g3 = unicode_dict["g3"], h3 = unicode_dict["h3"])
    row_3_line =  "    _________________________________"
    row_2 =       "2   | {a2} | {b2} | {c2} | {d2} | {e2} | {f2} | {g2} | {h2} |".format(a2 = unicode_dict["a2"], b2 = unicode_dict["b2"], c2 = unicode_dict["c2"], d2 = unicode_dict["d2"], e2 = unicode_dict["e2"], f2 = unicode_dict["f2"], g2 = unicode_dict["g2"], h2 = unicode_dict["h2"])
    row_2_line =  "    _________________________________"   
    row_1 =       "1   | {a1} | {b1} | {c1} | {d1} | {e1} | {f1} | {g1} | {h1} |".format(a1 = unicode_dict["a1"], b1 = unicode_dict["b1"], c1 = unicode_dict["c1"], d1 = unicode_dict["d1"], e1 = unicode_dict["e1"], f1 = unicode_dict["f1"], g1 = unicode_dict["g1"], h1 = unicode_dict["h1"])
    row_1_line =  "    _________________________________"



    # Now print these strings.
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




