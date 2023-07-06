"""
The Radiobutton is usable when you group (couple) a number (>1) of these widgets – as only one of them can be mutually selected (checked), it’s a good tool to represent one of many user choices. Assigning the same observable variable to more than one Radiobutton creates a group.

This also means that when two Radiobuttons use different observable variables, they belong to different groups by definition.

rdbutton = Radiobutton(master, option, ...)

Here are some of the Radiobutton’s properties:

Let's start with its properties:
Radiobutton property 	Property meaning
command 	the callback being invoked when the Radiobutton (not the group it belongs to!) changes its state
justify 	the same as for Button
state 	the same as for Button
variable 	an observable IntVar or StringVar variable reflecting the current selection within the Radiobutton’s group; changing the variable’s value automatically changes the selection
value 	a unique (inside the group) value identifying the Radiobutton; can be an integer value or a string, and should be compatible with the variable’s type

Some of the Radiobutton’s methods are shown here.

Note: there is no toggle() method as a single Radiobutton performs such an operation.
Radiobutton method 	Method role
deselect() 	unchecks the widget
flash() 	the same as for Button
invoke() 	the same as for Button
select() 	checks the widget

Run the sample code we've provided in the editor.

The program defines two separate Radiobutton groups, consisting of two Radiobuttons. These groups are coupled, as their callbacks change the opposite group to reflect the state of their own group. Thanks to that, you can choose a meal and change country, or you can change country and the meal will select itself automatically.

Let’s say “Goodbye” now – we’ll meet again soon to discuss some non-clickable widgets!

"""
import tkinter as tk
from tkinter import messagebox


def show():
    messagebox.showinfo("", "radio_1=" + str(radio_1_var.get()) +
                        ",radio_2=" + str(radio_2_var.get()))


def command_1():
    radio_2_var.set(radio_1_var.get())


def command_2():
    radio_1_var.set(radio_2_var.get())


window = tk.Tk()
button = tk.Button(window, text="Show", command=show)
button.pack()
radio_1_var = tk.IntVar()
radio_1_1 = tk.Radiobutton(window, text="pizza", variable=radio_1_var, value=1, command=command_1)
radio_1_1.select()
radio_1_1.pack()
radio_1_2 = tk.Radiobutton(window, text="clams", variable=radio_1_var, value=2, command=command_1)
radio_1_2.pack()
radio_2_var = tk.IntVar()
radio_2_1 = tk.Radiobutton(window, text="FR", variable=radio_2_var, value=2, command=command_2)
radio_2_1.pack()
radio_2_2 = tk.Radiobutton(window, text="IT", variable=radio_2_var, value=1, command=command_2)
radio_2_2.select()
radio_2_2.pack()
window.mainloop()
