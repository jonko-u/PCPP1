"""
One of the properties we want to tell you about is font. Every widget presenting a piece of text (e.g., Button and Label but not Frame) can be made to use a font different from the default.

Tkinter represents fonts as tuples. Surprised? Don’t be, it’s very simple.

Any font can be described as two- or three-element tuples:

("font_family_name", "font_size")

("font_family_name", "font_size", "font_style")

    the two-element tuple contains two strings: the first containing the font’s family name, and the second carrying the font’s size measured in points; note: the second element has to be a string, although it specifies strictly numerical information;
    the three-element tuple uses the third string to specify the font’s style, which can be expressed using the following strings:

        "bold"
        "italic"
        "underline"
        "overstrike"

Do you want to see it in action? Of course you do!

The property responsible for storing font information is – obviously – named font.

We’ve used the Label widget to demonstrate three different fonts. Look at the code in the editor.

Expand it to display some more fonts, including your favorite ones.

Our fonts look like this:
07.07.png

What about yours?
"""
import tkinter as tk


window = tk.Tk()
label_1 = tk.Label(window, text="Quick brown fox jumps over the lazy dog")
label_1.grid(column=0, row=0)
label_2 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Times", "12"))
label_2.grid(column=0, row=1)
label_3 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Arial", "16", "bold"))
label_3.grid(column=0, row=2)
window.mainloop()