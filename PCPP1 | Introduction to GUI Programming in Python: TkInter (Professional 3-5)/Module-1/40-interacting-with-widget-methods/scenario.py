"""
As you already know, widgets may or may not have the focus. At most one widget can have the focus. When you use a keyboard to interact with the application, you can use the Tab and Shift-Tab keys to move the focus forward and backward, but the focus can be controlled programmatically, too. There are two methods to help you cope with this issue. Assuming that Wi is an existing widget, the methods look as follows:

wi.focus_get()
wi.focus_set()

    the focus_get() method returns a reference to the currently focused widget, or None when no widget owns the focus (note: you can invoke the method from any widget, including the main window)
    the focus_set() method focuses the widget from the method which was invoked, so you have to choose it carefully.

Look at the code we've provided in the editor. This simple sample application shows how the focus can be moved between two buttons and uses the after() method to propel the process.

Try to add one or more buttons to the window and change the jumpthefocus() function to organize a cyclical focus journey around all the buttons.

We’ll say “goodbye” to widgets now, as we’re going to place the observable variables under our magnifying glass.

"""
import tkinter as tk


def flip_focus():
    if window.focus_get() is button_1:
        button_2.focus_set()
    else:
        button_1.focus_set()
    window.after(1000, flip_focus)


window = tk.Tk()
button_1 = tk.Button(window, text="First")
button_1.pack()
button_2 = tk.Button(window, text="Second")
button_2.pack()
window.after(1000, flip_focus)
window.mainloop()
