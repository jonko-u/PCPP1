"""
Note: we want the button_1 button to be filled (expanded) in the vertical direction:

This puzzle is a bit easier than the previous one. Think for a moment.

Yes, you're right – this is the expected answer.

We think that there is one intriguing question that can be asked here and now: do these buttons have to be gray? It's boring. Very boring.

We're going to clear up this issue soon.
"""
import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.pack(side=tk.RIGHT, fill=tk.Y)
button_2.pack()
button_3.pack()
window.mainloop()
