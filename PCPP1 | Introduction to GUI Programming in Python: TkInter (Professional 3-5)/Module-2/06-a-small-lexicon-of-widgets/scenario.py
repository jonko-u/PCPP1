"""
The Message widget is very similar to the Label (among other things, it has the same properties) but is able to format the presented text by fitting it automatically to the widget’s size.

message = Message(master, option, ...)

The sample code will tell you more.

Run it and see how the Message widget reacts to the tx variable updates.
"""
import tkinter as tk


def do_it_again():
    text.set(text.get() + "and again...")


window = tk.Tk()
button = tk.Button(window, text="Go ahead!", command=do_it_again)
button.pack()
text = tk.StringVar()
message = tk.Message(window, textvariable=text, width=400)
text.set("You did it again... ")
message.pack()
window.mainloop()
