"""
The main tkinter window has a method named bind_all() which binds a callback to all currently existing widgets.

There is also a method named unbind_all() which reverts the first method’s effects.

window.bind_all(event, callback)
window.unbind_all(event)

We used the bind_all() method to bind the one and the same callback to all three widgets, whether clickable or not. Look at the code we've provided in the editor.

Play with the code. Don’t worry, it’s safe.

Now we’re going to take you on a trip to Widget land. It’ll be an exciting journey, we promise.
"""
import tkinter as tk
from tkinter import messagebox


def hello(dummy):
    messagebox.showinfo("", "Hello!")


window = tk.Tk()
button = tk.Button(window, text="On/Off")
button.pack()
label = tk.Label(window, text="Label")
label.pack()
frame = tk.Frame(window, bg="yellow", width=100, height=20)
frame.pack()
window.bind_all("<Button-1>", hello)
window.mainloop()
