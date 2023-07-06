"""
Tkinter recognizes over 750 predefined color names – all of them can be found here.

Feel free to use them – we've showed our try in the editor.

This is what we get:
04.04-1.png


Yes, it definitely does:

The third method you can use is based on the fact that each color can be obtained by mixing (adding) three primary colors: red (R), green (G) and blue (B). The phenomenon is utilized by the so-called RGB color model which is one of the additive color models and it's widely used in many application, e.g. in color displays of different kinds.

One of the RGB model implementations allows you to set the saturation of every of primary colors in the range <0..255> what gives 256 different saturation levels, from color's absence (saturation 0) to full color's presence (saturation 255).

Do you think it's not too much? Maybe, but don't forget that you mix three different colors (so-called color components) so the full spectrum consists of 256*256*256 = 16,777,216 colors. An average human can distinguish about 7 million colors, consequently, the model should work well and it really does.

Let's take a closer look at this.

"""
import tkinter as tk


window = tk.Tk()
button = tk.Button(window, text="Button #1",
                   bg="MediumPurple",
                   fg="LightSalmon",
                   activeforeground="LavenderBlush",
                   activebackground="HotPink")
button.pack()
window.mainloop()
