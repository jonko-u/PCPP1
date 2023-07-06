"""
Widget methods

Widgets have methods – you’ve met some of them already. Now we’re going to show you a few more of them, and we’ll start with two which seem to be very specific. We can even say that the sense of their existence is very closely bound to the unique features of event programming.

The methods are named (assuming that Widget is an existing widget):

Widget.after(time_ms, function)

Widget.after_cancel(id)

    after() – this method expects two arguments: the first is a time interval specification (expressed in milliseconds: 1 s = 1000 ms) and the second points to an existing function; successful invocation of the method causes the event manager to change its plans; when the number of milliseconds elapses, the manager will invoke the function (only once); note: this the only possible way of controlling the passage of time when using an event-driven environment.

    Why? Because you can’t just invoke the built-in sleep() function within any of your callbacks – it would freeze your application for the whole nap time; the after() method returns a value which is as specific as the method itself – it’s a unique id of the planned invocation; is it usable? Yes, it is, e.g., when you are going to delete the previously planned invocation from the manager’s calendar, which is done with a method named…

    after_cancel(id) – the method cancels the planned invocation identified by the id argument.

Seems confusing? Not at all. The example will shed more light on it than telling you a long and winding story.

The code we’ve written to demonstrate how the after() method works is rather simple (yes, absolutely; don’t you think so, too?). You can see it in the editor window.

There’s a function named blink(), which changes the f framepackage’s background color from white to black and back depending on the state of the iswhite variable. Easy.

Note: there is no explicit invocation of the function inside the code. Moreover, it isn’t assigned as a callback. The question is – who invokes it?

The event managers do, because:

    we initially encourage it to make the invocation before the framepackage widget is packed into the main window;
    we continue to encourage it every time the blink() function is invoked – this gives the application the ability to blink as long as the application is running.

Try to change the delay time (the first method’s argument) and check how the application works then.
"""
import tkinter as tk


def blink():
    global is_white
    if is_white:
        color = 'black'
    else:
        color = 'white'
    is_white = not is_white
    frame.config(bg=color)
    frame.after(500, blink)


is_white = True
window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg='white')
frame.after(500, blink)
frame.pack()
window.mainloop()
