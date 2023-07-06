"""
Event handler

An event handler is a piece of code responsible for responding to all clicks addressed to our button.

The event handler we need has a simple assignment – we want it to just terminate our application. This crucial operation is done with a main window method called – don't be afraid – destroy(). It's a parameterless method, as destroying needs (in contrast to creation) no arguments at all.

How do we write the event handler?

It's a function. Just a simple function. The handler used by the button has to be a parameterless function of any name. Don't forget that the function will be invoked, not by us, but only by the controller.

Furthermore, invoking your own handler is strictly prohibited, as it can completely confuse the event controller.

We don't want the controller to be confused. It may end badly. Therefore, the simplest handler may look like this:

def Click():
    skylight.destroy()

Note: a function designed to be invoked by someone/something else (not us!) is often called a callback. We'll use the names handler and callback interchangeably.

Okay, we have a handler, but how do we couple it with the rest of the window's machinery?

Look carefully at the Button's constructor invocation - we've provided the code in the editor.

A new argument has appeared there. Its name is command, and it's set with the name of a callback that will be invoked when the button is clicked. Note: there are no parentheses, as we don't want to invoke the callback here – we need its name to be passed to the Button object.

Now we can run the code and check if our button is functional. We hope it is.

Two remarks should be made here:

    binding the callback with the widget by using the command constructor's parameter is not the only way offered by tkinter for this purpose; moreover, callbacks can be replaced during program execution – we'll tell you more about that soon;
    the one and same callback can be bound with more than one widget – it's a very useful solution in some cases.

"""
import tkinter


def Click():
    skylight.destroy()


skylight = tkinter.Tk()
skylight.title("Skylight")
button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)
skylight.mainloop()
