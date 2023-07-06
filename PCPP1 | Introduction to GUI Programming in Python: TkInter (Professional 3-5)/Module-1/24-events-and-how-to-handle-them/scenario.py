"""
In the editor we've provided a very simple code demonstrating how showinfo() works:

Note the \n embedded inside the info string.

And this is what the final message box looks like:
"""
import tkinter
from tkinter import messagebox


def clicked():
    messagebox.showinfo("info", "some\ninfo")


window = tkinter.Tk()
button_1 = tkinter.Button(window, text="Show info", command=clicked)
button_1.pack()
button_2 = tkinter.Button(window, text="Quit", command=window.destroy)
button_2.pack()
window.mainloop()