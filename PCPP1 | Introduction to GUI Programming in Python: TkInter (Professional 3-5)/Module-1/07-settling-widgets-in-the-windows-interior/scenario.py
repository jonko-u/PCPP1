"""
Look, we've added some arguments to the previous snippet. Two buttons (b1 and b2) should look different now – can we be sure of it?

Yes, we can!

As you can see, using place() gives you full control over the window's image. There is only one important but — full control means full responsibility. Sometimes it's better to share the responsibility among two parts – e.g., you and the grid() geometry controller.

grid() sees the window's area as a... grid. This means that the whole of the window's interior is divided into a number of columns of equal width and a number of rows of equal height.

The grid itself is not visible – the distribution is modeled inside the manager and you are only able to know its effects i.e., the widget's final arrangement.

You're not obliged to declare the number of rows and columns in advance – grid() finds the proper numbers for you. Let's try it.

"""
import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.place(x=10, y=10, width=150)
button_2.place(x=20, y=40)
button_3.place(x=30, y=70, height=50)
window.mainloop()
