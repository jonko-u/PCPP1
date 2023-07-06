"""
Objectives

Learn practical skills related to:

    using the Entry, Radiobutton and Button widgets,
    managing widgets with the grid manager,
    checking the validity of user input and handling errors.

Scenario

You need a calculator. A very simple and very specific calculator. Look at the picture - it contains two fields that the user can use to enter arguments, a radio button to select the operation to perform, and a button initiating the evaluation:

Calculator - reference

We expect the calculator to behave in the following way:

    if both fields contain valid (integer or float) numbers, clicking the Evaluate button should display an info window showing the evaluation's result;
    if any of the fields contains invalid data (e.g., a string, or a field is empty), clicking the Evaluate button should present an error window describing the problem, and the focus should be moved to the field causing the problem.

Don't forget to protect your code from dividing by zero, and use the grid manager to compose the window interior.

"""

from tkinter import *
from tkinter import messagebox


def evaluate():
    a = float(e1.get())
    b = float(e2.get())
    if op.get() == "Addition":
        result = a + b
    elif op.get() == "Subtraction":
        result = a - b
    elif op.get() == "Multiplication":
        result = a * b
    elif op.get() == "Division":
        if b == 0:
            messagebox.showerror("Error", "Cannot divide by 0")
            e2.focus_set()
            return
        result = a / b
    messagebox.showinfo("Result", str(result))


root = Tk()
root.title("Calculator")

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=0, padx=10, pady=10)
e2.grid(row=1, column=0, padx=10, pady=10)

op = StringVar()
op.set("Addition")

r1 = Radiobutton(root, text="Addition", variable=op, value="Addition")
r2 = Radiobutton(root, text="Subtraction", variable=op, value="Subtraction")
r3 = Radiobutton(root, text="Multiplication", variable=op, value="Multiplication")
r4 = Radiobutton(root, text="Division", variable=op, value="Division")
r1.grid(row=2, column=0, sticky=W, padx=10, pady=10)
r2.grid(row=3, column=0, sticky=W, padx=10, pady=10)
r3.grid(row=4, column=0, sticky=W, padx=10, pady=10)
r4.grid(row=5, column=0, sticky=W, padx=10, pady=10)

b = Button(root, text="Evaluate", command=evaluate)
b.grid(row=6, column=0, padx=10, pady=10)

root.mainloop()