"""
If you want your main window to be sized in a non-default way, you have to use a low-level method named geometry(), whose only argument looks a bit exotic, as it’s a string. Yes, a string.

The string is constructed in the following way:

width x height

where width and height are decimal numbers specifying both dimensions in pixels.

Note: you can use this invocation at any time, but you have to take into consideration how the change can influence all your widgets.

Our sample code in the editor shows you how to use it.

Look – clicking the window changes its size, and the window gets bigger and smaller periodically.

Note the method we use to build a geometry() argument.
"""
import tkinter as tk


def click(*args):
    global size, grows
    if grows:
        size += 50
        if size >= 500:
            grows = False
    else:
        size -= 50
        if size <= 100:
            grows = True
    window.geometry(str(size) + "x" + str(size))


size = 100
grows = True
window = tk.Tk()
window.geometry("100x100")
window.bind("<Button-1>", click)
window.mainloop()
