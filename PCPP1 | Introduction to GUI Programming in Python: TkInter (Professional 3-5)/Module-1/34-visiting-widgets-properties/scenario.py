"""
Every widget occupies a part of the window’s area, thus it’s obvious the widgets must have sizes. Interestingly, widgets have properties describing many more sizes than just width (usually specified in pixels) and height (which can be specified in rows of text if the widget is able to present textual information).

The list of widget sizes is gathered in the table:
Widget property name 	Property role
borderwidth 	The width of the 3D-framepackage surrounding some widgets (e.g., Button)
highlightthickness 	The width of the additional framepackage drawn around the widget when it gains the focus
padx

pady 	The width/height of an additional empty space/margin around the widget
wraplength 	If the text filling the widget becomes longer than this property’s value, it will be wrapped (possibly more than once)
height 	The height of the widget
underline 	The index of the character inside the widget’s text, which should be presented as underlined or -1 otherwise (the underlined letter/digit can be used as a shortcut key, but it needs a specialized callback to work – no automation here, sorry)
width 	The width of the widget

The example in the editor shows how some of the sizes work.

This is what we see on our screen:


07.10.png

Do you see the same?
"""
import tkinter as tk


window = tk.Tk()
button_1 = tk.Button(window, text="Ordinary button");
button_1.pack()
button_2 = tk.Button(window, text="Exceptional button")
button_2.pack()
button_2["borderwidth"] = 10
button_2["highlightthickness"] = 10
button_2["padx"] = 10
button_2["pady"] = 5
button_2["underline"] = 1
window.mainloop()
