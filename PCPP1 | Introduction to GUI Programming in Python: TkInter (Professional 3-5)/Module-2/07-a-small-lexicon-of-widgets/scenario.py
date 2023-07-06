"""
The Frame widget is, in fact, a container designed to store other widgets. This means that the Frame can be used to separate a rectangular part of the window and to treat it as a kind of local window. Such a window works as a master widget for all the widgets embedded within it. Moreover, the Frame has its own coordinate system, so when you place a widget inside a Frame, you measure its location relative to the Frame’s upper-left corner, not the window’s one. It also means that if you move the Frame to a new position, all its inner widgets will go with it.

Note: the Frame can grasp virtually any widget – including another Frame.

The Frame has one interesting property:
Frame property 	Property meaning
takefocus 	normally, the Frame doesn’t take the focus (which would seem to be obvious) but if you really want it to behave in this way, you can set the property to 1.

Take a look at the example in the editor.

We’ve defined two separate frames and filled them with two buttons each. Note: we’ve used different geometry managers for both Frames. This is another advantage of the Frame – it helps you arrange the window in the most convenient way.

Pay attention to all four of the Buttons’ constructors – how have we described a master widget there?

"""
import tkinter as tk

window = tk.Tk()

frame_1 = tk.Frame(window, width=200, height=100, bg='white')
frame_2 = tk.Frame(window, width=200, height=100, bg='yellow')

button_1_1 = tk.Button(frame_1, text="Button #1 inside Frame #1")
button_1_2 = tk.Button(frame_1, text="Button #2 inside Frame #1")
button_2_1 = tk.Button(frame_2, text="Button #1 inside Frame #2")
button_2_2 = tk.Button(frame_2, text="Button #2 inside Frame #2")

button_1_1.place(x=10, y=10)
button_1_2.place(x=10, y=50)
button_2_1.grid(column=0, row=0)
button_2_2.grid(column=1, row=1)

frame_1.pack()
frame_2.pack()

window.mainloop()
