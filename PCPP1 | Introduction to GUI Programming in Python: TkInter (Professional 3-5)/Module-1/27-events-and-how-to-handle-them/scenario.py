"""
Let’s modify our code again. We want it to unveil some info coming in with the event object. Look at the code in the editor.

We encourage you again to carry out some experiments with this code. Use it to discover the event’s anatomy in detail.

A callback bound to a certain event may be unbound at any moment.

Let’s analyze the process in relation to clickable widgets i.e., those having the command property and using the command constructor’s parameter.

If you unbind a callback from an event, the widget stops reacting to the event. If you want to reverse this action, you must bind the callback again.

We haven’t said a word on modifying a widget’s properties, and we’re going to discuss it thoroughly in the next section, so please forgive us for only doing it briefly now.

If you want to modify a property named prop, existing within a widget named wid, and you’re going set its value to val, you can use the config() method, just like here:

wid.config(prop=val)

This means that if you want to unbind your current callback from a Button named b1, you would use an invocation like this one:

b1.config(command=lambda:None)

This binds an empty (i.e., doing absolutely nothing) function to the widget’s callback.

Let’s test it.
"""
import tkinter as tk
from tkinter import messagebox


def click(event=None):
    if event is None:
        tk.messagebox.showinfo("Click!", "I love clicks!")
    else:
        string = "x=" + str(event.x) + ",y=" + str(event.y) + \
                 ",num=" + str(event.num) + ",type=" + event.type
        tk.messagebox.showinfo("Click!", string)


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click)
frame.pack()

window.mainloop()
