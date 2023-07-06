"""
Our new friend is called Label – a non-clickable widget able to present short textual information, passed to the widget's constructor using a text argument. The text can later be changed at any moment of the widget's life.

As you can see, we're using the pack() geometry manager to compose the window.

Let's welcome Label into our window:

Note: pack() resizes the window to a size large enough to fit all the packed widgets. This is its default behavior. Don't worry, the window will grow soon.

"""
import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text = "Little label:")
label.pack()

window.mainloop()