"""
Non-clickable widgets

The next four widgets fall into the non-clickable category. They’re designed to present textual information and don’t have a command property, although you can use bind() to simulate similar behavior.

The Label widget displays some lines of text inside the window:

label = Label(master, option, ...)

The Label widget contains two usable properties, but you need to remember that they are mutually exclusive.

Here you are:
Label property 	Property meaning
text 	a string which will be shown within the Label; note: newline characters (\n) are interpreted in the usual way
textvariable 	the same as for text, but makes use of an observable StringVar variable, so if you change the variable’s alteration, it will be immediately visible on the screen.

The Label widget has no usable methods – sorry!

The sample in the editor shows how the textvariable accompanied by an observable variable can be used to continuously update the Label’s contents.
"""
import tkinter as tk


def to_string(x):
    return "Current counter\nvalue is:\n" + str(x)


def plus():
    global counter
    counter += 1
    text.set(to_string(counter))


counter = 0
window = tk.Tk()
button = tk.Button(window, text="Go on!", command=plus)
button.pack()
text = tk.StringVar()
label = tk.Label(window, textvariable=text, height=4)
text.set(to_string(counter))
label.pack()
window.mainloop()
