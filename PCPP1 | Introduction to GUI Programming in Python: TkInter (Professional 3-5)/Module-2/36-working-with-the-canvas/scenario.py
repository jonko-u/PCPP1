"""
Drawing a polygon looks very similar to drawing a line, with the difference being that the last segment (connecting the first and the last points) in the chain is drawn automatically (you don’t need to specify the same point as the first and the last (x,y) pair:

canvas.create_polygon(x0, y0, x1, y1, xn, yn, option...)

The method uses the same set of options as create_polygon().

Do you want to see it in action? Check out the code we've provided in the editor.

Analyze it and try to predict the shape it produces.
"""
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='black')
canvas.create_polygon(20, 380, 200, 68, 380, 380, outline='red', width=5, fill='yellow')
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
