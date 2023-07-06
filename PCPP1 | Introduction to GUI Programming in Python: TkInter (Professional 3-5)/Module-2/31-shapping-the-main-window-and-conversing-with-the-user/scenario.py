"""
If you need to display some error information, you can use the showerror() function. It displays a red warning icon and doesn’t ask any questions – its only button is titled OK.

It also returns a string OK in every case.

See the sample code we've provided in the editor.

"""
import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.showerror("!", "Your code does nothing!")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="Alarming message", command=question)
button.pack()
window.mainloop()
