"""
Take a look at the code in the editor pane. The sample we’ve prepared for you makes use of the checkbutton and does two things:

    counts all the checkbutton’s state changes and stores the result in cnt variable;
    presents the current cnt value and the checkbutton’s state after clicking the Show button.

"""
import tkinter as tk
from tkinter import messagebox


def count():
    global counter
    counter += 1

def show():
    messagebox.showinfo("","counter=" + str(counter) + ",state=" + str(switch.get()))


window = tk.Tk()
switch = tk.IntVar()
counter = 0
button = tk.Button(window, text="Show", command=show)
button.pack()
checkbutton = tk.Checkbutton(window, text="Tick", variable=switch, command=count)
checkbutton.pack()
window.mainloop()
