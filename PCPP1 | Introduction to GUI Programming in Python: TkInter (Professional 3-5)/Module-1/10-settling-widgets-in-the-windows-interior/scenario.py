"""
We've ordered pack() to push the button_1 button to the right window's boundary.

Can you predict the window's appearance? We admit that it may be difficult.

Is this what you expected?
03.15.png

No? Are you surprised? You have the right to be. Pack is the least intuitive geometry manager for sure, and you really need to spend some time testing its whims.

We have one more experiment left to carry out.
"""
import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.pack(side=tk.RIGHT)
button_2.pack()
button_3.pack()
window.mainloop()
