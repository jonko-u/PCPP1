"""
Our next companion will be Frame.

A Frame is another non-clickable component used to group widgets and to separate them (visually) from other window components. Our Frame plays a less important role – it just occupies a rectangle and fills it with its own color. We expect nothing more for now.

Let's check it out.

This is how the Frame manifests its presence:
05.06.png

Make our window great again.
"""
import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

window.mainloop()
