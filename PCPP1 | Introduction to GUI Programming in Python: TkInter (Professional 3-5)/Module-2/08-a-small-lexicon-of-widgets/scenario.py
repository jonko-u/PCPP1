"""
The LabelFrame widget is a Frame enriched with a visible border and a title (also visible). The title may be located at one of 12 possible places on the border line.

lfrm = LabelFrame(master, option, ...)

Some of the usable LabelFrame properties are gathered here:
LabelFrame property 	Property meaning
takefocus 	the same as for the Frame
text 	the LabelFrame’s title
labelanchor 	the title’s location, defined as a string containing a quasi-compass coordinate (as shown by the image)


LabelFrame coordinates


We’ve rebuilt our previous example to employ a LabelFrame instead of a Label – look at the updated code we've provided in the editor.

Run it and find the differences.
"""
import tkinter as tk

window = tk.Tk()
label_frame_1 = tk.LabelFrame(window, text="Frame #1",
                              width=200, height=100, bg='white')
label_frame_2 = tk.LabelFrame(window, text="Frame #2",
                              labelanchor='se', width=200, height=100, bg='yellow')

button_1_1 = tk.Button(label_frame_1, text="Button #1 inside Frame #1")
button_1_2 = tk.Button(label_frame_1, text="Button #2 inside Frame #1")
button_2_1 = tk.Button(label_frame_2, text="Button #1 inside Frame #2")
button_2_2 = tk.Button(label_frame_2, text="Button #2 inside Frame #2")

button_1_1.place(x=10, y=10)
button_1_2.place(x=10, y=50)
button_2_1.grid(column=0, row=0)
button_2_2.grid(column=1, row=1)

label_frame_1.pack()
label_frame_2.pack()
window.mainloop()
