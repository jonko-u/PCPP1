"""
If you want to bind your own callback to the main window’s close operation (which can be caused by the user clicking the window’s closing button), you can use a low-level tkinter method named protocol() in the following way:

protocol("WM_DELETE_WINDOW", callback)

The sample shows one of the possible ways of using this mechanism.
"""
import tkinter as tk
from tkinter import messagebox


def really():
    if messagebox.askyesno("?", "Wilt thou be gone?"):
        window.destroy()


window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", really)
window.mainloop()
