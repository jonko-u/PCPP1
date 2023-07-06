"""
The create_text() method puts text on the Canvas. The text is placed inside a rectangle whose center is located at point (x,y):

c.create_text(x, y, option...)

The method makes use of the following options:
Option name 	Option meaning
fill 	text color
font 	text font
justify 	text justification: LEFT (default), CENTER, RIGHT
text 	text to display (\n works as expected)
width 	normally, the rectangle is as wide as the longest text line; using the width option forces the text to be aligned to that size

This is what the create_text() method can do for you (and much more as well).
14.15.png
"""
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='blue')
canvas.create_text(200, 200, text="Mary\nhad\na\nlittle\nlamb",
                   font=("Arial","40","bold"),
                   justify=tk.CENTER,
                   fill='white')
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
