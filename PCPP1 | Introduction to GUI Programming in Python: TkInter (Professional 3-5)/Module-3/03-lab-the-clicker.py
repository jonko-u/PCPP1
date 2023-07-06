"""
Objectives

Learn practical skills related to:

    writing event handlers and assigning them to widgets using the bind() method,
    managing widgets with the grid manager,
    using the after() and after_cancel() methods.

Scenario

We want you to write a simple but challenging game, which can help many people to improve their perception skills and visual memory. We'll call the game The Clicker as clicking is what we expect from the player.

The Clicker's board consists of 25 buttons and each of the buttons contains a random number from range 1..999. Note: each number is different!

Below the board there is a timer which initially shows 0. The timer starts when the user clicks the board for the first time.

Here's how we imagine The Clicker's initial board state:

The Clicker - initial board's state

We expect the player to click all the buttons in the order imposed by the numbers - from the lowest to the highest one. Additional rules say that:

    the properly clicked button changes the button's state to DISABLED (it greys the button out)
    the improperly clicked button shows no activity,
    the timer increases its value every second,
    when all the buttons are greyed out (i.e., the player has completed his/her task) the timer stops immediately.

This is how the board looks when the game is finished:

The Clicker - final board's state

Hint: consider using the <Button-1> event instead of setting the command button property - it may simplify your code.
"""

import tkinter as tk
from tkinter import messagebox
import random

class ClickerGame:
    def __init__(self, master):
        self.master = master
        self.master.title("The Clicker")
        self.buttons = []
        self.current_button = 0
        self.timer_value = 0
        self.create_widgets()
        self.master.bind("<Button-1>", self.handle_click)
        self.timer_label = tk.Label(self.master, text="Timer: 0")
        self.timer_label.grid(row=5, column=0, columnspan=5)
        self.timer_label.bind("<Button-1>", self.start_timer)

    def create_widgets(self):
        numbers = random.sample(range(1, 1000), 25)
        button_coords = random.sample([(i, j) for i in range(5) for j in range(5)], 25)
        for i in range(25):
            row, col = button_coords[i]
            button = tk.Button(self.master, text=str(numbers[i]), state=tk.NORMAL)
            button.grid(row=row, column=col)
            self.buttons.append(button)
        self.buttons.sort(key=lambda x: int(x["text"]))

    def handle_click(self, event):
        if event.widget in self.buttons:
            button_index = self.buttons.index(event.widget)
            if button_index == self.current_button:
                # Correct button clicked
                event.widget["state"] = tk.DISABLED
                event.widget["bg"] = "gray"
                self.current_button += 1
                # Change color of following buttons in the sequence
                for i in range(self.current_button, len(self.buttons)):
                    if int(self.buttons[i]["text"]) == self.current_button:
                        self.buttons[i]["state"] = tk.DISABLED
                        self.buttons[i]["bg"] = "gray"
                        self.current_button += 1
                        # Check if all buttons have been clicked
                        if self.current_button == len(self.buttons):
                            self.master.after_cancel(self.timer_id)
                            self.disable_buttons()
                            self.show_win_message()
                        break
                else:
                    # No button found with correct value, incorrect click, do nothing
                    pass

    def disable_buttons(self):
        for button in self.buttons:
            button["state"] = tk.DISABLED

    def start_timer(self, event):
        if self.current_button == 0:
            self.timer_id = self.master.after(1000, self.update_timer)

    def update_timer(self):
        self.timer_value += 1
        self.timer_label["text"] = "Timer: " + str(self.timer_value)
        if self.current_button < len(self.buttons):
            self.timer_id = self.master.after(1000, self.update_timer)
        else:
            self.show_win_message()

    def show_win_message(self):
        message = "¡Has ganado en {} segundos!".format(self.timer_value)
        messagebox.showinfo("¡Felicidades!", message)

root = tk.Tk()
game = ClickerGame(root)
root.mainloop()