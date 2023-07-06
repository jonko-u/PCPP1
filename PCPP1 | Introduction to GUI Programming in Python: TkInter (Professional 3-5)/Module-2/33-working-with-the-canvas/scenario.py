"""
Take a look at the code.

It creates a 400 x 400-pixel canvas with a yellow background. Next, it draws a line (precisely: a polygonal chain) consisting of three line segments. The application can be terminated using the Quit button.

Can you find the parts of the code responsible for all these actions?
14.02.png

First, we’ll show you how to create a canvas. This is done with a constructor named Canvas().

c = Canvas(master, options...)

Its first argument specifies the master widget (as usual). A set of keyword arguments specifies the properties of the canvas. The most usable of them are as follows:
Property name 	Property role
borderwidth 	canvas border’s width in pixels (default: 2)
background (bg) 	canvas border’s color (default: the same as the underlying window’s color)
height 	canvas height (in pixels)
width 	canvas width (in pixels)
"""
import tkinter as tk


window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
