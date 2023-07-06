"""
Let's check if tkinter understands English – look at the code in the editor, our test is there.

Note the two new arguments we use in the constructor invocation: bg (what is a short form of “background-color”) and fg (“foreground-color”). We went along the line of least resistance here – we've just made use of regular English names of colors and packed them inside strings.

Does it work? Let's check.

Yes, it definitely does:

We encourage to you make some clicks on the button – it will unveil its little secret.

Can you see? The colors of the lowered (pressed) button are gray still. Why?

Because fb and bg refer to raised buttons only. There two additional parameters describing the second set of colors named activeforeground and activebackground respectively used by the event controller when the button is pressed. Do you want to check how they work? Do it boldly!

We can summarize the test's result saying that any of commonly used English color name can be used with tkinter. Don't bother if you want some of your widgets to be simply white, black, green, gray or even grey. It's easy and handy although not very precise.

Tkinter can do something more for you.
"""
import tkinter as tk

window = tk.Tk()
button = tk.Button(window, text="Button #1", bg="red", fg="yellow")
button.pack()
window.mainloop()
