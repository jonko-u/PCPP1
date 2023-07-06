"""
When you want to warn your user about any threat, use the showwarning() function – it’ll present a warning icon and always returns OK.
"""
import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.showwarning("Be careful!", "Big Brother is watching you!")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="What's going on?", command=question)
button.pack()
window.mainloop()
