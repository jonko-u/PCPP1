"""
The askokcancel() function is very similar, but it creates a dialog equipped with two buttons titled OK and Cancel (it returns True for OK and False otherwise).

You can observe its behavior by running the code we've provided in the editor.
"""
import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.askokcancel("?", "I'm going to format your hard drive")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="What are your plans?", command=question)
button.pack()
window.mainloop()
