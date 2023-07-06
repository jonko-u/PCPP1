"""
There’s also a method called maxsize(), which protects the window from becoming too large.

Check the code in the editor window to see how it works.
"""
import tkinter as tk

window = tk.Tk()
window.maxsize(width=500, height=300)
window.geometry("200x200")
window.mainloop()
