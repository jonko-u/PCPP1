"""
The askquestion() function uses a different return value. It displays two buttons titled Yes and No along with a question mark icon, but returns a string Yes when the user’s answer is positive and No otherwise.

Check the code in the editor to see this in action.
"""
import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.askquestion("?", "I'm going to format your hard drive")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="What are your plans?", command=question)
button.pack()
window.mainloop()
