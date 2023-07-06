"""
We’ve added two widgets at once – look!

These are the Radiobuttons, small circles filled with a dot, or not. The most important difference between Check- and Radiobuttons lies in the fact that Checkbuttons are solitary (they work individually) while Radiobuttons always work in groups and – note it! – only one of the widgets inside the group can be checked. Clicking an unchecked member of the group will cause the currently checked Radiobutton to change its state.

How do we achieve such an effect? The switch object will help us with it.

Our two Radiobutton constructors use two additional arguments. What roles do they play?

    The variable argument binds a switch object to both of the widgets, and this is the clue – the fact that both Radiobuttons are bound to the same object creates the group. Don’t forget that!
    The value argument distinguishes the Radiobuttons inside the group, and thus each of the Radiobuttons has to use a different value (we’ve used 0 and 1)

The communication through the switch object should work as follows:

    selecting one of the Radiobuttons affects the switch object, which changes its value to one of the possible values specified in the Radiobuttons’ constructor; note: the mechanism works in the same way if there are more Radiobuttons in the group;
    simultaneously, changing the switch object’s state affects the Radiobutton group.

As the switch is initially set to 1, we expect the second Radiobutton (named Salad) to be selected when the application starts.

Do you want to check it? Go ahead!
"""
import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

button = tk.Button(window, text ="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
checkbutton.pack()

entry = tk.Entry(window, width=30)
entry.pack()

radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)
radiobutton_1.pack()
radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)
radiobutton_2.pack()

window.mainloop()
