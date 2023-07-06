"""
The next step adds a brand new widget to our window – it’s a Checkbutton.

It’s a small square which can be filled with a tick mark, or which can be empty.

The Checkbutton is primarily used to represent two-state selections. In other words, it can be in one of two possible states:

    the ON state when the Checkbutton is checked/ticked (which can be equated with an affirmative answer to some question)
    the OFF state when the Checkbutton is cleared (you can think of it as a kind of negative answer)

Take a look at the Checkbutton constructor – there’s something completely new. Can you see it?

Yes, it’s a variable argument. Note – it’s set to the previously created switch object. The assignment creates a bidirectional link between the object and the widget. How does it work?

    If you check or uncheck the Checkbutton, the switch object will immediately change its state – it will keep 0 if the widget is unchecked, and 1 otherwise.
    If you change the state of the switch object, the Checkbutton will immediately reflect the change – it means that you don’t need to access the Checkbutton itself to check/uncheck it, as you can modify the switch value instead.

Look, the switch is initially set to 1. this means that the Checkbutton will be checked when it appears on the screen.

Let's check it.
"""
import tkinter as tk

win = tk.Tk()

label = tk.Label(win, text="Little label:")
label.pack()

frame = tk.Frame(win, height=30, width=100, bg="#000099")
frame.pack()

button = tk.Button(win, text="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

checkbutton = tk.Checkbutton(win, text="Check Button", variable=switch)
checkbutton.pack()

win.mainloop()
