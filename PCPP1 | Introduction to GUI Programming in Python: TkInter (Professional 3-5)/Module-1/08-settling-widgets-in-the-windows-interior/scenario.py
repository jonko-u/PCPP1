"""
Can you see what we changed in the code?

Yes, we modified the third grid() invocation a bit. We wanted to deploy the button inside the cell located in the third (actually, the lowest) row and the first (the left-most) column, but we also did something else – we wanted the widget to span across two horizontally neighboring cells.

We admit that this puzzle is somewhat harder than the previous ones. Don't rush through this – think it over carefully.

Here's the solution.

Note: the manager noticed that the total number of columns is actually two, not three as in the previous code. This is why the window looks different.

The third, fully automatic geometry manager is named pack() as it packs subsequent widgets into the window's interior. This means that the order in which the widgets are packed matters – in contrast to grid() and place().

Let's take a look at it.
"""
import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.grid(row=0, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=2, column=0, columnspan=2)
window.mainloop()
