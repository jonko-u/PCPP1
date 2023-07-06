"""
Look at the code in the editor. We want to show you you a little test showing how the RGB works:

Do the colors look the same as in the previous code?

They should look the same as we used RGB equivalents of the previously used tkinter color names.

Now try to find RGB codes for all your favorite colors. There are so many choices – don't feel lost!

"""
import tkinter as tk

window = tk.Tk()
button = tk.Button(window, text="Button #1",
                   bg="#9370DB",
                   fg="#FFA07A",
                   activeforeground="#FFF0F5",
                   activebackground="#FF69B4")
button.pack()
window.mainloop()
