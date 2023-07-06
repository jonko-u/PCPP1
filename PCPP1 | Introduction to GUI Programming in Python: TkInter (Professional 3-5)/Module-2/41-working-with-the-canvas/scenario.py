"""
If you want to use a JPEG bitmap, some additional steps are required – you need to:

    import the Image and ImageTk classes from the PIL (Python Image Library) module;
    build an object of the Image() class and use its open() method to fetch the bitmap from the file (the argument should specify the file’s path)
    convert this object into a PhotoImage class object using an ImageTk function of the same name;
    continue as usual.

The example in the editor will tell you more.

This is how it works.

14.19.png

So... we gave you a canvas, paints, and brushes – are you ready to paint a masterpiece?
"""
import tkinter as tk
import PIL

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='red')
jpg = PIL.Image.open('logo.jpg')
image = PIL.ImageTk.PhotoImage(jpg)
canvas.create_image(200, 200, image=image)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
