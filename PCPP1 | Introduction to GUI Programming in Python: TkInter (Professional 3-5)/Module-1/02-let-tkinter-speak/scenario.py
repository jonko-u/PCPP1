"""Did you get the same window as ours?


There are some issues with the window, and the most important is how to close it while also causing the application to quit. Currently, there is no other way than to make use of some of the OS's default behaviors, e.g., clicking the closing button (ours is red – and yours?) or using a dedicated keyboard shortcut like MS Windows®' Alt-F4.

A preferable way of coping with that is to equip the window with a dedicated button, but now we're going to make a little cosmetic change. We don't like the window's title. We'll change it now. How?

Each window (including the main one) has a method named – of course – title(). The method can be invoked more than once in any moment of the window's life. We'll activate it before the window is shown, just like the way we do it in the editor window.

Can you see it? The title has changed now!"""
import tkinter

skylight = tkinter.Tk()
skylight.title("Skylight")
skylight.mainloop()
