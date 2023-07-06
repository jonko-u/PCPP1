"""
The default pack's operation tends to deploy all subsequent widgets in one column, one below the other. You can change this behavior to a limited extent by using the following parameters:

    side=s – forces the manager to pack the widgets in a specified direction, where s can be specified as:
        TOP – the widget is packed toward the window's top (it's manager's default behavior)
        BOTTOM – the widget is packed toward the window's bottom;
        LEFT – toward the window's left boundary;
        RIGHT – toward the window's right boundary;
    fill=f – suggests to the manager how to expand the widget if you want it to occupy more space than the default, while f should be specified as:
        NONE – do not expand the widget (default behavior)
        X – expand it in the horizontal direction;
        Y – expand it in the vertical direction;
        BOTH – expand it in both directions;

We want to warn you that the results produced by pack() can be extremely surprising, and you should spend some time on your own experimenting with all its vices.

We suggest you use it only as a temporary solution to help you get a working application quickly, but if you want your application to look nice and to be legible and clear (of course, you would want that!) you'd better forget about pack() and use either grid() (in simpler cases) or place().

Let pack() show us what it can do for us. Look at the code in the editor.

As you can see, using pack() simplifies the code – you don't need to specify any coordinates – but that doesn't mean this will simplify the developer's life. You may expect that pack() will know how to handle your widgets, but sometimes it's work results are like a lottery.

Let's look at the window we get. The window looks different.
03.13.png

Very different. For example, the window fits its size to the area occupied by the widgets. The buttons are located one after the other, from top to bottom.

Let's play a little game with pack's arguments.
"""
import tkinter as tk


window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.pack()
button_2.pack()
button_3.pack()
window.mainloop()
