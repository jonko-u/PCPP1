"""
Level of difficulty

Hard
Objectives

Learn practical skills related to:

    dealing with observable variables,
    working with the Entry widget,
    constructing complex interfaces with many cooperating Button widgets.

Scenario

Have you ever used an ordinary pocket calculator? We prefer to ask you first as we're aware of the fact that these devices went out of fashion some time ago and they were replaced with computer and smartphone's applications.

This is exactly what we want you to implement - a simple, four-function "pocket" calculator. Feel free to equip it with many extra functions, but adding, subtracting, multiplying and dividing is a must - there is no calculator without these operations.

Moreover, the calculator needs a change sign function, a decimal point button and the clear button. We don't have to mention that your calculator should be resistant to zero-division attempts, in which case it should display an error message instead of producing any garbage result or raising an exception.

The screenshots we present below are just a suggestion. You can design the UI in a different way, and it will be good as long as your calculator works properly. We aren't able to collect all strict requirements in one place - we can only say that each time you have doubts about how to implement a particular behavior, you should just pick up a real pocket calculator and check how it works in the specific context.

See how we've implemented our GUI (initial state, presenting a result, and handling zero-division attempt) - do you like it?

Calculator at initial state Calculator presenting a result Calculator after zero-divide attempt

Here are some of our assumptions:

    respond only to mouse clicks; keyboard presses can be silently ignored,
    the display's width is 10 - use a fixed-width font to work with it,
    you are not allowed to fill the display with more than 10 characters (including the decimal point and minus sign if it is needed); if the result needs more characters to be presented, you should display an error message,
    you are allowed to remove some less significant digits located after the decimal point to shorten the result in effect,
    if the result has no significant digits after the decimal point, the point should not appear on the display.


"""
import tkinter as tk


class Calculator:

    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.result = tk.StringVar()
        self.result.set('0')
        self.operator = ''
        self.operand = 0
        self.create_widgets()

    def create_widgets(self):
        # Create a label for the display.
        label = tk.Label(self.master, textvariable=self.result, font=('Arial', 20), width=16, anchor='e')
        label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons for digits 0-9.
        digits = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
        for i, digit in enumerate(digits):
            button = tk.Button(self.master, text=digit, width=5, height=2, font=('Arial', 16),
                               command=lambda digit=digit: self.add_digit(digit))
            button.grid(row=2 + (i // 3), column=i % 3, padx=5, pady=5)

        # Create buttons for each operation.
        operations = ['+', '-', '*', '/']
        for i, operation in enumerate(operations):
            button = tk.Button(self.master, text=operation, width=5, height=2, font=('Arial', 16),
                               command=lambda operation=operation: self.set_operator(operation))
            button.grid(row=i + 1, column=3, padx=5, pady=5)

        # Create buttons for special functions.

        button_clear = tk.Button(self.master, text="C", width=5, height=2, font=('Arial', 16),
                                 command=lambda: self.clear())
        button_clear.grid(row=1, column=0, padx=5, pady=5)

        button_zero = tk.Button(self.master, text="0", width=5, height=2, font=('Arial', 16),
                               command=lambda digit="0": self.add_digit(digit))
        button_zero.grid(row=5, column=0, padx=5, pady=5)

        button_decimal = tk.Button(self.master, text=".", width=5, height=2, font=('Arial', 16),
                                   command=lambda: self.add_decimal())
        button_decimal.grid(row=5, column=2, padx=5, pady=5)

        button_sign = tk.Button(self.master, text="+/-", width=5, height=2, font=('Arial', 16),
                                command=lambda: self.change_sign())
        button_sign.grid(row=5, column=1, padx=5, pady=5)

        button_equals = tk.Button(self.master, text="=", width=5, height=2, font=('Arial', 16),
                                  command=lambda: self.calculate())
        button_equals.grid(row=5, column=3, padx=5, pady=5)

    def add_digit(self, digit):
        if self.result.get() == '0':
            self.result.set(digit)
        else:
            self.result.set(self.result.get() + digit)

    def add_decimal(self):
        if '.' not in self.result.get():
            self.result.set(self.result.get() + '.')

    def change_sign(self):
        self.result.set(str(-float(self.result.get())))

    def set_operator(self, operator):
        self.operator = operator
        self.operand = float(self.result.get())
        self.result.set('0')

    def calculate(self):
        if self.operator == '+':
            result = self.operand + float(self.result.get())
        elif self.operator == '-':
            result = self.operand - float(self.result.get())
        elif self.operator == '*':
            result = self.operand * float(self.result.get())
        elif self.operator == '/':
            divisor = float(self.result.get())
            if divisor == 0:
                result = "Error: division by zero"
            else:
                result = self.operand / divisor

        try:
            # Check if result has too many digits after decimal point
            if isinstance(result, float) and abs(result) >= 1e10:
                result = "Error: result too large"
            else:
                # Truncate result to 10 characters (including decimal point and minus sign)
                result_str = "{:.10f}".format(result)
                # Remove trailing zeros and decimal point if not needed
                result_str = result_str.rstrip('0').rstrip('.')
                if result_str == '-0':
                    result_str = '0'
                if len(result_str) > 10:
                    result = "Error: result too long"
                else:
                    result = result_str

            self.result.set(result)
            self.operator = ''
            self.operand = 0
        except:
            self.result.set("ERROR: Divided by Zero")
    def clear(self):
        self.result.set('0')
        self.operator = ''
        self.operand = 0

    # Define the functions for each operation.
    def add(self):
        """Adds the two numbers in the display."""
        first_number = int(self.result.get())
        second_number = int(input("Enter the second number: "))
        total = first_number + second_number
        self.result.set(str(total))

    def subtract(self):
        """Subtracts the second number from the first number in the display."""
        first_number = int(self.result.get())
        second_number = int(input("Enter the second number: "))
        total = first_number - second_number
        self.result.set(str(total))

    def multiply(self):
        """Multiplies the two numbers in the display."""
        first_number = int(self.result.get())
        second_number = int(input("Enter the second number: "))
        total = first_number * second_number
        self.result.set(str(total))

    def divide(self):
        """Divides the first number by the second number in the display."""
        first_number = int(self.result.get())
        second_number = int(input("Enter the second number: "))
        total = first_number / second_number
        self.result.set(str(total))


root = tk.Tk()
calc = Calculator(root)
root.mainloop()