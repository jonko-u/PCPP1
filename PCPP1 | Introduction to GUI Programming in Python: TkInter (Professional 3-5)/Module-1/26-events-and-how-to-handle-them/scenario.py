""""
Don’t be afraid if some of the events look a bit suspicious. You’ll get used to them soon.

Note:

    a callback designed for usage with the command property/parameter is a parameterless function;
    a callback intended to cooperate with the bind() method is a one-parameter function (the callback’s argument carries some info about the captured event)
    fortunately, it doesn’t mean that you have to define two different callbacks for those two applications, and this is how we’ll cope with the above requirements:

    def callback(ev=None):
        :
        :

    the callback will work flawlessly in both of these contexts, and moreover, it’ll give you the chance to identify which one of the two possible styles of launch has just occurred.

We’re going to change our previous example a bit by making it sensitive to more than just one click.

We've provided the newer version of our code in the editor.

Pay attention to Line I and Line II in the above code. They show the way in which you can bind your callback to any of non-clickable widgets. The bind remains active to the end of the application’s work, but you can also manually unbind the event at any moment (and bind it again when you wish).

We encourage you to play with the code – test the behavior of some of the other events. It’ll be fun... we think.

We’ve said previously that an event is actually an object. Let’s shed some light on that.
"""
import tkinter as tk
from tkinter import messagebox


def click(event=None):
    tk.messagebox.showinfo("Click!", "I love clicks!")


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)   # Line I
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click)   # Line II
frame.pack()

window.mainloop()
