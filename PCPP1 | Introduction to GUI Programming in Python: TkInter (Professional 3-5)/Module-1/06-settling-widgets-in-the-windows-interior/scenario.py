"""
The place geometry manager demands the usage of the place() method. Note: the method is invoked from within the widget's object, not the window, as the widget is always aware of the window it belongs to (it gets the information from the constructor's very first argument).

The most usable place() method parameters are as follows (all of them are passed as keyword arguments):

    height=h – the widget's desired height measured in pixels; if the parameter is omitted, the widget's height will be determined automatically;
    width=w – the widget's desired width measured in pixels; if the parameter is omitted, the widget's width will be determined automatically;
    x=x – the widget's top-left pixel's horizontal coordinate measured relative to the home window's top-left corner;
    y=y – the widget's top-left pixel's vertical coordinate measured relative to the home window's top-left corner.

Let's see them all in action.

The snippet we've prepared for you shows how the place() method works. Look at the code in the editor.

It places three buttons in a cascade-like order. Try to guess what these buttons will look like inside the window. Yes, this is what we expected, isn't it?
03.03.png

Now let's play with width and height for a moment.
"""
import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.place(x=10, y=10)
button_2.place(x=20, y=40)
button_3.place(x=30, y=70)
window.mainloop()
