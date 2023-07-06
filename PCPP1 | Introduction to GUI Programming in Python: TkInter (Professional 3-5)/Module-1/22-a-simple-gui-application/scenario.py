"""
This is what our window looks like now:
05.11.png

Okay, it definitely looks as expected, but how can we be sure that the switch object changes its state according to our clicks addressed to the Checkbutton?

We’ll show you soon. Stay tuned.

Now we add a very important, and internally an extremely complicated, widget, named Entry. Look at the code in the editor.

Entry is designed to let the user enter simple, one-line data, like single numbers, names, addresses, etc.

We’ve added one to our window. It creates an input field 30 characters wide. You can play with it if you want, but it’s completely inoperative as far. We only want to show you what it looks like.

Isn’t our window lovely?
05.13.png

Okay, let’s provide some serious work to our switch object.

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

checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
checkbutton.pack()

entry = tk.Entry(window, width=30)
entry.pack()

window.mainloop()
