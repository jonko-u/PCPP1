"""
The main window is a very specific construct, as its fate is shared among two masters: you (supported by tkinter) and your operating system. This means than you cannot manage the window like any other widget, as the OS must be aware of anything you do with the main window.

The first main window property that you may want to change is its title. The title is defaultly set to Tk, no matter what your application is named, or even if it's unnamed.

To change the window’s title, you would use a method named title().

Our sample code shows a window which changes its title each time you click over it, until you do it ten times, after which the title remains 0.
"""
import tkinter as tk


def click(*args):
    global counter
    if counter > 0:
        counter -= 1
    window.title(str(counter))


counter = 10
window = tk.Tk()
window.title(str(counter))
window.bind("<Button-1>", click)
window.mainloop()
