"""
The first method is based on using a dictionary which exists inside every widget. Assuming that a widget named Widget has a property named prop and you want to read its value and then set it with a new value, you can do this in the following way:

old_val = Widget["prop"]

Widget["prop"] = new_val

Let’s see it in action. Look at the example we've provided in the editor.

Note: we use the text property to:

    diagnose the current button’s state;
    change the button’s state to the contrary one;
    update the button’s title.

Run the code and observe its behavior.

"""
import tkinter as tk


def on_off():
    global button
    state = button["text"]
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button["text"] = state


window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
window.mainloop()
