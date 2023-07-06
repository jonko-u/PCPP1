"""
Our application creates a window with two buttons in it. The first one works as an on/off switch, while the switch changes the behavior of the second button. When the switch is ON, clicking the second button activates a message box. When the switch if OFF, clicking the second button has no effect. Moreover, the second button’s title changes according to the switch’s state.

Note the method we use to change the button’s title.

The two faces of our window look like this:
06.19-1.png


06.19-2.png

Now we’ll do the same trick again, but this time with the non-clickable widget.

To unbind a callback previously bound with the bind() method invocation, you need to use the unbind() method:

widget.unbind(event)

The method requires one argument identifying the event being unbound.

Note: the information about a previously used callback is lost. You cannot retrieve it automatically and you must repeat the bind() invocation.

Let’s jump into the code.
"""
import tkinter as tk
from tkinter import messagebox


def on_off():
    global switch
    if switch:
        button_2.config(command=lambda: None)
        button_2.config(text="Gee!")
    else:
        button_2.config(command=peekaboo)
        button_2.config(text="Peekaboo!")
    switch = not switch


def peekaboo():
    messagebox.showinfo("", "PEEKABOO!")


def do_nothing():
    pass


switch = True
window = tk.Tk()
buton_1 = tk.Button(window, text="On/Off", command=on_off)
buton_1.pack()
button_2 = tk.Button(window, text="Peekaboo!", command=peekaboo)
button_2.pack()
window.mainloop()
