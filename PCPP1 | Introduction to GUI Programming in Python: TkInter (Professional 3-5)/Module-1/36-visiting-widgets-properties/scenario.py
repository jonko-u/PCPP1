"""
Our next widget is an anchor. Don’t worry, we aren’t going to take you out to sea. We’ll stay on dry land, we promise. The anchor is an imaginary (invisible) point inside the widget to which the text (if any) is anchored. As you’ve probably noticed, widgets tend to put their text in the middle of themselves (both in horizontal and vertical directions). The location of the anchor can easily be changed, as there is a property of the same name.

It seems to be obvious, but there’s one unobvious aspect – how to name the anchors.

This is done by a set of predefined identifiers which make of use of the compass coordinates – take a look and everything will be clear at once:
Compass coordinates.png

As you can see, there are nine anchors, and the one placed in the middle is named CENTER (not a very compassey name, we admit). The CENTER anchor is the default one and is used when you don’t set the anchor property at all.

Let’s do some tests.

Look at the code in the editor. We’ve used two buttons to show two non-default anchors – we hope you’ll continue our experiments on your own.

Our buttons look as follows – and yours?
"""
import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Regular button")
button_1["anchor"] = "e"
button_1["width"] = 20  # pixels!
button_1.pack()
button_2 = tk.Button(window, text="Another button")
button_2["anchor"] = "sw"
button_2["width"] = 20
button_2["height"] = 3  # rows
button_2.pack()
window.mainloop()
