from tkinter import *
from math import sqrt
import numpy as np


def create_circle(x,y,r,width):
    canvas.create_oval(x-r, y-r, x+r, y+r, outline='blue',width=width)
    
def create_line(x1,y1,x2,y2):
    canvas.create_line(x1,y1,x2,y2,width=3)

def draw_bezier_curve(x1,y1,x2,y2,x3,y3,x4,y4):

    number = 50
    # x1,y1 = points[0][0],points[0][1]
    # x2,y2 = points[1][0],points[1][1]
    # x3,y3 = points[2][0],points[2][1]
    # x4,y4 = points[3][0],points[3][1]
    x = None
    y = None
    points1 = np.array([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])

    matrix = np.array([[-1, 3, -3, 1],
                                 [3, -6, 3, 0],
                                 [-3, 3, 0, 0],
                                 [1, 0, 0, 0]])
    t_value = np.linspace(0, 1, number)
    for t in t_value:
        T = np.array([t**3, t**2, t, 1])
        point = np.dot(T, np.dot(matrix, points1))
        x_new, y_new = point[0],point[1]
        if x != None:
            create_line(x,y,x_new,y_new)
        x=x_new
        y=y_new

def reset_canvas():
    canvas.delete("all")

# Create the window and canvas
root = Tk()
canvas = Canvas(root, width=1200, height=800)
canvas.pack()

# Create a frame inside the canvas
frame = Frame(canvas, width=1200, height=300)
canvas.create_window(600, 0, window=frame)
frame.configure(bg='white')

# create the input field
input_field = Entry(root)
input_field.place(relx=0.6, rely=0.03, anchor='ne',)
input_field.insert(0,"30")


# add a label next to the input field
label = Label(root, text="Enter the number of lines:")
label.place(relx=0.4, rely=0.03, anchor='ne')



# create reset botton
button1 = Button(root, text="Reset", command=reset_canvas)
button1.place(relx=0.75, rely=0.043, anchor='center')


# Create circle
x, y, r = 1000, 600, 30
x1, y1, r1 = 1000, 600, 50
create_circle(900, 570, 40,3)
create_circle(900, 570, 70,3)

create_circle(500, 600, 20,3)
create_circle(500, 600, 40,3)

create_line(460,640,1000,640)  # create ground line

draw_bezier_curve(1000,550, 950,420, 800,420, 800,600)

draw_bezier_curve(570,600, 550,550, 520,520, 480,530)

create_line(800,600,570,600)

create_line(480,530,480,420)

create_line(480,420,960,420)
create_line(960,420,960,485)

create_line(530,420,530,320)

create_line(720,420,760,300)
create_line(760,300,900,300)
create_line(900,300,900,420)

# Start the main loop
root.mainloop()