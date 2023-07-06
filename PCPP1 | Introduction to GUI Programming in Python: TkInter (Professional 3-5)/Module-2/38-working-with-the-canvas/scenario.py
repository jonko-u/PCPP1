"""If you want to draw an arc (a part of an ellipse) you’ll use the create_arc() method:

canvas.create_arc(x0,y0,x1,y1,option...)

The method draws the arc of an ellipse inscribed inside a rectangle with vertices at points (x0,y0) and (x1,y1).

The options are the same as for create_polygon(), and define a set of three new ones, specific to the method:
Option name 	Option meaning
style 	can be set to one of the following: PIESLICE (default), CHORD and ARC; the shape of the resulting drawing is presented here:

Pieslice, chord & arch.png

start 	the angle (in degrees) of the arc’s start relative to the X-axis (e.g., 90 means the highest point of the ellipse, while 0 is the right-most point. The default is 0)
extent 	the arc’s span (in degrees) relative to the start point; note: the span is calculated counter-clockwise. The default is 90 (a quarter of an ellipse)

Take a look at the code in the editor, this is how we’ve done it. Try to imagine what it looks like!

14.13.png"""
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
canvas.create_arc(10, 100, 380, 300, outline='red', width=5)
canvas.create_arc(10, 100, 380, 300, outline='blue', width=5,
                  style=tk.CHORD, start=90, fill='white')
canvas.create_arc(10, 100, 380, 300, outline='green', width=5,
                  style=tk.ARC, start=180, extent=180)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
