"""
Drawing an ellipse (and a circle is, in fact, a specific ellipse) needs a method named create_oval():

c.create_eclipse(x0,y0,x1,y1,xn,yn,option...)

The method draws an ellipse inscribed in a rectangle with vertices at the points (x0,y0) and (x1,y1).

If the rectangle is a square, the ellipse becomes a circle.

The options are the same as for create_polygon().

Let’s test it. Run the code we've provided in the editor.

Is it an ellipse or a circle? What do you think?
"""
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='blue')
canvas.create_oval(100, 100, 300, 200, outline='red', width=20, fill='white')
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
