"""
The destroy() method

The destroy() method is very destructive. It removes the widget completely, not only from your sight, but also from the event manager’s memory, as the widget’s object is deleted and becomes inaccessible.

wi.destroy()

Do you remember? We used this method to close the main window and to stop the whole application. You can use the method in a less devastating manner to get rid of unnecessary widgets while keeping the application alive.

Note: if the widget you want to destroy has children (when other widgets are embedded inside it, which can happen with frames) the children will be destroyed, too (this rule works recursively).

The example prepares a window filled with a framepackage that is the parent of one Button. Note – we’ve ordered the event manager to activate the suicide() function during the 5th second of application life.

The function destroys the framepackage, but first it destroys all the framepackage’s children and its children’s children and … okay, let’s end the story here . It’s infinite – telling it will take too much time.

Run the code and check how it works.
"""
import tkinter as tk


def suicide():
    frame.destroy()


window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg='green')
button = tk.Button(frame, text="I'm a framepackage's child")
button.place(x=10, y=10)
frame.after(5000, suicide)
frame.pack()
window.mainloop()
