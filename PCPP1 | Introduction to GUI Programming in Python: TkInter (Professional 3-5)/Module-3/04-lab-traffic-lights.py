"""Objectives

Learn practical skills related to:

    dealing with Canvas and some of its methods,
    using different colors.

Scenario

Look at the snippet in the editor - can you see that mysterious tuple consisting of four three-element tuples? Can you guess what information it carries?

It's a set of rules describing the behavior of British-style traffic lights. Assume that the very first element of all inner tuples is assigned to the red light, the second - to the yellow, and the third - to the green one. True means that the light is on, False - off.

As you see, there are four different phases:

    the red light is lit,
    the red and yellow lights are lit together,
    the green light is lit,
    the yellow light is lit.

Your task is to implement a model which will show how such a traffic signal works. The model should look as follows:

Red Red-Yellow Green Yellow

As you see, the model is built of three widgets:

    the canvas being a background for all the three lights,
    the button named "Next" - clicking it switches the signal to the next phase,
    the button named "Quit" - clicking it immediately exits the program.

Note: use the phases tuple as a "knowledge base" for your whole code. The code has to adopt to any change done to the tuple, e.g., there can be more or less than four phases and the lights' combinations can be different also.

If traffic lights in your home country work in a different way, you can implement your native scheme, but the only change you're allowed to make is to modify the phases tuple - the code itself must remain the same.
"""

from tkinter import Tk, Button, Canvas

phases = ((True, False, False),
          (True, True, False),
          (False, False, True),
          (False, True, False))

class TrafficSignal:
    def __init__(self, master):
        self.master = master
        self.master.title("Traffic Signal")
        self.phase_index = 0
        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(self.master, width=100, height=250, bg='black')
        self.canvas.pack(side='left', padx=5, pady=5)

        self.red_light = self.canvas.create_oval(25, 25, 75, 75, fill='black', outline='black')
        self.yellow_light = self.canvas.create_oval(25, 100, 75, 150, fill='black', outline='black')
        self.green_light = self.canvas.create_oval(25, 175, 75, 225, fill='black', outline='black')

        self.next_button = Button(self.master, text='Next', command=self.next_phase)
        self.next_button.pack(side='top', padx=5, pady=5)

        self.quit_button = Button(self.master, text='Quit', command=self.master.quit)
        self.quit_button.pack(side='top', padx=5, pady=5)

        self.update_lights()

    def update_lights(self):
        for i in range(3):
            if phases[self.phase_index][i]:
                self.canvas.itemconfig([self.red_light, self.yellow_light, self.green_light][i], fill=['red', 'yellow', 'green'][i])
            else:
                self.canvas.itemconfig([self.red_light, self.yellow_light, self.green_light][i], fill='black')

    def next_phase(self):
        self.phase_index = (self.phase_index + 1) % len(phases)
        self.update_lights()

root = Tk()
traffic_signal = TrafficSignal(root)
root.mainloop()