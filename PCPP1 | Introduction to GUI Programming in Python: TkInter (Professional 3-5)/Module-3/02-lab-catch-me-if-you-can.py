"""
Objectives

Learn practical skills related to:

    using screen coordinates,
    managing widgets with the place manager,
    binding events using the bind() method.

Scenario

Write a simple game - an infinite game which humans cannot win. Here are the rules:

    the game goes on between TkInter and the user (probably you)
    TkInter opens a 500x500 pixel window and places a button saying "Catch me!" in the top-left corner of the window;
    if the user moves the mouse cursor over the button, the button immediately jumps to another location inside the window; you have to assure that the new location is distant enough to prevent the user from making an instant click,
    the button must not cross the window's boundaries during the jump!

Here is a sample picture for your reference:
"""

import tkinter as tk
import random

root = tk.Tk()
root.title("Catch me!")
root.geometry("500x500")

button = tk.Button(root, text="Catch me!")
button.place(x=0, y=0)

def move_button(event):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    button.place(x=x, y=y)

button.bind("<Motion>", move_button)

root.mainloop()