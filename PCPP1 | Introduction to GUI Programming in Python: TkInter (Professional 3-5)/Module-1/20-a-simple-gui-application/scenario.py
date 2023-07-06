"""
Our next component is completely invisible. You won't find it in the window area.

It's the switch variable. Can't you see it? It's set to hold an object of the IntVar class. This object is designed to store integer values. "Okay," you may say, "can't we use a regular variable instead?"

No, we can't. Objects of the IntVar class are used by tkinter to organize internal communication between different widgets. A regular variable can't play such a role.

If you want such an object to store an integer value, you can't use the assignment operator. The class offers a dedicated method for that purpose, and the method is named set().

Note: we've used the method to store a value of 1 inside the object.

As the window's view hasn't changed, we can go directly to the next step.

"""
import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

button = tk.Button(window, text="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

window.mainloop()
