"""
Our next property is the cursor.

As you know, the default mouse cursor reveals itself as an arrow. Sometimes, when it enters a specific area, its shape can change (e.g., over input fields).

You have the power to order the cursor to change to a different cursor over each of the widgets, as every widget has the property we’re talking about.

Unfortunately, the repertoire of available cursors isn’t very impressive – all of them are described here.

We’ll show you three of them. Feel free to test all the rest. Don’t forget to move the cursor over the frames. You won’t see anything interesting without doing that.

Okay. Now we’re ready to show you some of the widget methods. You’re familiar with some of them already. See you soon!

"""
import tkinter as tk

window = tk.Tk()
label_1 = tk.Label(window, height=3, text="arrow", cursor="arrow")
label_1.pack()
label_2 = tk.Label(window, height=3, text="clock", cursor="clock")
label_2.pack()
label_3 = tk.Label(window, height=3, text="heart", cursor="heart")
label_3.pack()
window.mainloop()
