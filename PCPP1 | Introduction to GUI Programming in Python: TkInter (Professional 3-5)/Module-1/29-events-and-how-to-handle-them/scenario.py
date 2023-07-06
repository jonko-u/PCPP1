"""
The application contains two widgets: one Button (clickable) and one Label (non-clickable).

We bind a callback to the Label, causing it to display (in a loop) the first five words of this old but good rhyme (please dive into the rhyme() function to check out how we’ve done it).

This functionality can be turned off and on by clicking the button. As you can see, the on_off() callback binds and unbinds the label’s callback.

Try to modify the code to use a few other events to trigger the switch.
"""
import tkinter as tk


def on_off():
    global switch
    if switch:
        label.unbind("<Button-1>")
    else:
        label.bind("<Button-1>", rhyme)
    switch = not switch


def rhyme(dummy):
    global word_no, words
    word_no += 1
    label.config(text=words[word_no % len(words)])


switch = True
words = ["Old", "McDonald", "Had", "A", "Farm"]
word_no = 0
window = tk.Tk()
button = tk.Button(window, text="On/Off", command=on_off)
button.pack()
label = tk.Label(window, text=words[0])
label.bind("<Button-1>", rhyme)
label.pack()
window.mainloop()
