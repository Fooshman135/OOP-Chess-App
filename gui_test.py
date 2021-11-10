import PySimpleGUIQt as sg      
# import PySimpleGUI as sg      




legend_width = 10
board_side_length = 400
square_side_length = board_side_length / 8


my_layout = [
	[
		sg.Graph(canvas_size=(legend_width, legend_width), graph_bottom_left=(0,legend_width), graph_top_right=(legend_width, 0), background_color=None, key='spacer'), 
		sg.Graph(canvas_size=(board_side_length, legend_width), graph_bottom_left=(0,legend_width), graph_top_right=(board_side_length, 0), background_color=None, key='top_legend')
		],

	[
		sg.Graph(canvas_size=(legend_width, board_side_length), graph_bottom_left=(0,board_side_length), graph_top_right=(legend_width, 0), background_color=None, key='left_legend'), 
		sg.Graph(canvas_size=(board_side_length, board_side_length), graph_bottom_left=(0,board_side_length), graph_top_right=(board_side_length, 0), background_color='red', key='board')
		],


	# [sg.T(canvas_size=(50, 400), graph_bottom_left=(0,0), graph_top_right=(400, 50), background_color='white', key='graph_1'), sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0,0), graph_top_right=(400, 400), background_color=None, key='graph')],
	[sg.T(text="It is now someone's turn!", auto_size_text=True, background_color='white', text_color='black')],


]




"""
layout = [      
		   [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0,0), graph_top_right=(400, 400), background_color='red', key='graph')],      
		   [sg.T('Change circle color to:'), sg.Button('Red'), sg.Button('Blue'), sg.Button('Move')]      
		   ]      
"""


# my_window = sg.Window(title='Chess', layout=my_layout, margins=(0, 0), finalize=True)   
my_window = sg.Window(title="Ben's Chess App", layout=my_layout, finalize=True)       




# left_legend = window['left_legend']  
# n1 = left_legend.draw_text('1', (2,390), color='black')


#import ipdb
#ipdb.set_trace()
#point = my_window['top_legend'].DrawPoint(point=(0,0), size=10, color='blue') 


top_offset = -7		# In theory this shouldn't be necessary.
left_offset = 5		# In theory this shouldn't be necessary.


for i in range(8):
	letter = chr(97 + i)      # chr(97) produces the ASCII value "a"
	# my_window['top_legend'].draw_text(text=letter, location=(square_side_length/2 + square_side_length*i,legend_width/2), color='black', font = ("Courier New", 20), text_location=sg.TEXT_LOCATION_CENTER)
	# my_window['left_legend'].draw_text(text=str(8-i), location=(legend_width/2, square_side_length/2 + square_side_length*i), color='black', font = ("Courier New", 20), text_location=sg.TEXT_LOCATION_CENTER)

	my_window['top_legend'].draw_text(text=letter, location=(square_side_length/2 + top_offset + square_side_length*i,legend_width/2), color='black', font = ("Courier New", 20))
	my_window['left_legend'].draw_text(text=str(8-i), location=(legend_width/2, square_side_length/2 + left_offset + square_side_length*i), color='black', font = ("Courier New", 20))



graph = my_window['board']  

a8 = graph.DrawRectangle(top_left=(0,0), bottom_right=(50,50), fill_color='white', line_color='black')
a7 = graph.DrawRectangle(top_left=(0,50), bottom_right=(50,100), fill_color='black', line_color='black')
a6 = graph.DrawRectangle(top_left=(0,100), bottom_right=(50,150), fill_color='white', line_color='black')
a5 = graph.DrawRectangle(top_left=(0,150), bottom_right=(50,200), fill_color='black', line_color='black')
a4 = graph.DrawRectangle(top_left=(0,200), bottom_right=(50,250), fill_color='white', line_color='black')
a3 = graph.DrawRectangle(top_left=(0,250), bottom_right=(50,300), fill_color='black', line_color='black')
a2 = graph.DrawRectangle(top_left=(0,300), bottom_right=(50,350), fill_color='white', line_color='black')
a1 = graph.DrawRectangle(top_left=(0,350), bottom_right=(50,400), fill_color='black', line_color='black')

b8 = graph.DrawRectangle(top_left=(50,0), bottom_right=(100,50), fill_color='black', line_color='black')
b7 = graph.DrawRectangle(top_left=(50,50), bottom_right=(100,100), fill_color='white', line_color='black')
b6 = graph.DrawRectangle(top_left=(50,100), bottom_right=(100,150), fill_color='black', line_color='black')
b5 = graph.DrawRectangle(top_left=(50,150), bottom_right=(100,200), fill_color='white', line_color='black')
b4 = graph.DrawRectangle(top_left=(50,200), bottom_right=(100,250), fill_color='black', line_color='black')
b3 = graph.DrawRectangle(top_left=(50,250), bottom_right=(100,300), fill_color='white', line_color='black')
b2 = graph.DrawRectangle(top_left=(50,300), bottom_right=(100,350), fill_color='black', line_color='black')
b1 = graph.DrawRectangle(top_left=(50,350), bottom_right=(100,400), fill_color='white', line_color='black')

c8 = graph.DrawRectangle(top_left=(100,0), bottom_right=(150,50), fill_color='white', line_color='black')
c7 = graph.DrawRectangle(top_left=(100,50), bottom_right=(150,100), fill_color='black', line_color='black')
c6 = graph.DrawRectangle(top_left=(100,100), bottom_right=(150,150), fill_color='white', line_color='black')
c5 = graph.DrawRectangle(top_left=(100,150), bottom_right=(150,200), fill_color='black', line_color='black')
c4 = graph.DrawRectangle(top_left=(100,200), bottom_right=(150,250), fill_color='white', line_color='black')
c3 = graph.DrawRectangle(top_left=(100,250), bottom_right=(150,300), fill_color='black', line_color='black')
c2 = graph.DrawRectangle(top_left=(100,300), bottom_right=(150,350), fill_color='white', line_color='black')
c1 = graph.DrawRectangle(top_left=(100,350), bottom_right=(150,400), fill_color='black', line_color='black')

d8 = graph.DrawRectangle(top_left=(150,0), bottom_right=(200,50), fill_color='black', line_color='black')
d7 = graph.DrawRectangle(top_left=(150,50), bottom_right=(200,100), fill_color='white', line_color='black')
d6 = graph.DrawRectangle(top_left=(150,100), bottom_right=(200,150), fill_color='black', line_color='black')
d5 = graph.DrawRectangle(top_left=(150,150), bottom_right=(200,200), fill_color='white', line_color='black')
d4 = graph.DrawRectangle(top_left=(150,200), bottom_right=(200,250), fill_color='black', line_color='black')
d3 = graph.DrawRectangle(top_left=(150,250), bottom_right=(200,300), fill_color='white', line_color='black')
d2 = graph.DrawRectangle(top_left=(150,300), bottom_right=(200,350), fill_color='black', line_color='black')
d1 = graph.DrawRectangle(top_left=(150,350), bottom_right=(200,400), fill_color='white', line_color='black')

e8 = graph.DrawRectangle(top_left=(200,0), bottom_right=(250,50), fill_color='white', line_color='black')
e7 = graph.DrawRectangle(top_left=(200,50), bottom_right=(250,100), fill_color='black', line_color='black')
e6 = graph.DrawRectangle(top_left=(200,100), bottom_right=(250,150), fill_color='white', line_color='black')
e5 = graph.DrawRectangle(top_left=(200,150), bottom_right=(250,200), fill_color='black', line_color='black')
e4 = graph.DrawRectangle(top_left=(200,200), bottom_right=(250,250), fill_color='white', line_color='black')
e3 = graph.DrawRectangle(top_left=(200,250), bottom_right=(250,300), fill_color='black', line_color='black')
e2 = graph.DrawRectangle(top_left=(200,300), bottom_right=(250,350), fill_color='white', line_color='black')
e1 = graph.DrawRectangle(top_left=(200,350), bottom_right=(250,400), fill_color='black', line_color='black')

f8 = graph.DrawRectangle(top_left=(250,0), bottom_right=(300,50), fill_color='black', line_color='black')
f7 = graph.DrawRectangle(top_left=(250,50), bottom_right=(300,100), fill_color='white', line_color='black')
f6 = graph.DrawRectangle(top_left=(250,100), bottom_right=(300,150), fill_color='black', line_color='black')
f5 = graph.DrawRectangle(top_left=(250,150), bottom_right=(300,200), fill_color='white', line_color='black')
f4 = graph.DrawRectangle(top_left=(250,200), bottom_right=(300,250), fill_color='black', line_color='black')
f3 = graph.DrawRectangle(top_left=(250,250), bottom_right=(300,300), fill_color='white', line_color='black')
f2 = graph.DrawRectangle(top_left=(250,300), bottom_right=(300,350), fill_color='black', line_color='black')
f1 = graph.DrawRectangle(top_left=(250,350), bottom_right=(300,400), fill_color='white', line_color='black')

g8 = graph.DrawRectangle(top_left=(300,0), bottom_right=(350,50), fill_color='white', line_color='black')
g7 = graph.DrawRectangle(top_left=(300,50), bottom_right=(350,100), fill_color='black', line_color='black')
g6 = graph.DrawRectangle(top_left=(300,100), bottom_right=(350,150), fill_color='white', line_color='black')
g5 = graph.DrawRectangle(top_left=(300,150), bottom_right=(350,200), fill_color='black', line_color='black')
g4 = graph.DrawRectangle(top_left=(300,200), bottom_right=(350,250), fill_color='white', line_color='black')
g3 = graph.DrawRectangle(top_left=(300,250), bottom_right=(350,300), fill_color='black', line_color='black')
g2 = graph.DrawRectangle(top_left=(300,300), bottom_right=(350,350), fill_color='white', line_color='black')
g1 = graph.DrawRectangle(top_left=(300,350), bottom_right=(350,400), fill_color='black', line_color='black')

h8 = graph.DrawRectangle(top_left=(350,0), bottom_right=(400,50), fill_color='black', line_color='black')
h7 = graph.DrawRectangle(top_left=(350,50), bottom_right=(400,100), fill_color='white', line_color='black')
h6 = graph.DrawRectangle(top_left=(350,100), bottom_right=(400,150), fill_color='black', line_color='black')
h5 = graph.DrawRectangle(top_left=(350,150), bottom_right=(400,200), fill_color='white', line_color='black')
h4 = graph.DrawRectangle(top_left=(350,200), bottom_right=(400,250), fill_color='black', line_color='black')
h3 = graph.DrawRectangle(top_left=(350,250), bottom_right=(400,300), fill_color='white', line_color='black')
h2 = graph.DrawRectangle(top_left=(350,300), bottom_right=(400,350), fill_color='black', line_color='black')
h1 = graph.DrawRectangle(top_left=(350,350), bottom_right=(400,400), fill_color='white', line_color='black')






"""
graph = window['graph']   
circle = graph.DrawCircle((75,75), 25, fill_color='black',line_color='white')      
point = graph.DrawPoint((75,75), 10, color='green')      
oval = graph.DrawOval((25,300), (100,280), fill_color='purple', line_color='purple'  )      
rectangle = graph.DrawRectangle((25,300), (100,280), line_color='purple'  )      
line = graph.DrawLine((0,0), (100,100))  
"""    



while True:      
	event, values = my_window.read()      
	if event == sg.WIN_CLOSED:      
		break



"""
	if event is 'Blue':      
		graph.TKCanvas.itemconfig(circle, fill = "Blue")      
	elif event is 'Red':      
		graph.TKCanvas.itemconfig(circle, fill = "Red")      
	elif event is 'Move':      
		graph.MoveFigure(point, 10,10)      
		graph.MoveFigure(circle, 10,10)      
		graph.MoveFigure(oval, 10,10)      
		graph.MoveFigure(rectangle, 10,10)

"""






