"""
The create_image() method draws an image (a bitmap) on the Canvas. The image is placed inside a rectangle whose center is located at point (x, y):

canvas.create_image(x, y, option...)

The method needs an image to display, and the image is passed as a keyword argument:
Option name 	Option meaning
image 	an object of the PhotoImage class containing the image itself; the PhotoImage class constructor needs a keyword argument named file pointing to a bitmap file (note: only GIF and PNG formats are accepted); the argument should specify the file’s path

Let's see it inside our code.

Do you like our logo? We love it!
14.17.png
"""
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
image = tk.PhotoImage(file='logo.png')
canvas.create_image(200, 200, image=image)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
