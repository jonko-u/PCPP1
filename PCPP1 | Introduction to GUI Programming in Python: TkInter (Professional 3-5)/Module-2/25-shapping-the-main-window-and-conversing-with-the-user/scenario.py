"""
If you want your window to be completely inflexible and stiff, you’ll make use of the method named resizable(). It uses two parameters named width and height, but they accept Boolean values, not integer values. Their meaning is:

    True – the user can change this dimension;
    False – the user can’t change this dimension.

Setting both arguments to False will stiffen your window completely.

Check it out!

Normally, destroying any of the existing widgets causes the event manager to run an event named <Delete>, which enables the other widgets to react. Unfortunately, this doesn’t work with the main window.

"""
import tkinter as tk

window = tk.Tk()
window.resizable(width=False, height=False)
window.geometry("400x200")
window.mainloop()
