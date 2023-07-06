"""
You already know the three alternative methods used to describe the colors. Now we’ll show you which parts of the widget can be colorized. There are more options than you may suspect:
Widget property name 	Property role
background

bg 	The color of the widget’s background (you can freely use either of these two forms)
foreground

fg 	The color of the widget’s foreground (note: it can mean different things in different widgets; in general, it’s used to specify text color)
activeforeground

activebackground 	Like bg and fg but used when the widget becomes active
disabledforeground 	The width of the widget

Let’s colorize a button – look at the code in the editor, this is how we’ve done it.

And this is what it looks like in both inactive and active states:

07.10-1.png

Inactive

07.10-2.png

Active

You don't like the colors? Feel free to experiment with the colors of the font, foreground, and background to make the button look more attractive.
"""
import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Ordinary button");
button_1.pack()
button_2 = tk.Button(window, text="Colorful button")
button_2.pack()
button_2.config(bg ="#000000")
button_2.config(fg ="yellow")
button_2.config(activeforeground ="#FF0000")
button_2.config(activebackground ="green")
window.mainloop()
