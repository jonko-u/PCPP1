"""If you like to have full control over all your source code, you can make the import process extremely itemized by importing each of the facilities separately – just like this:

from tkinter import Button

If you're an enthusiast of living life on the edge, you can simplify your import (but not the rest of your work) by using the star as a component name:

from tkinter import *

It's handy when you write it, but it can bring some cumbersome troubles when names from the package's namespace cross with some of your private names.

Don't think we're going to discourage you from using this form. It's only a warning. Or rather a piece of friendly advice.

Now we're ready to create our first application. The application will be completely mute, deaf to the same extent as it is mute, and thus completely indifferent to any input. Don't worry, we'll breathe some life into it soon – it's only a very first step.

Look at the code in the editor.

The main application window (which is often the only window being used by the application) is created by the tkinter method named Tk(). In its most commonly used form, it needs no arguments. The object returned by the method is complete, but at the same time, completely invisible. Moreover, it won't be visible until the event controller starts.

To start the controller, you have to invoke the main window's method, named mainloop().

The name is significant because – as you can see – there is nothing more you can do in your code. Entering the controller's main loop deprives you of the possibility of direct control over the code's execution. Now you're fully at the mercy of the controller. Exiting the main loop is equivalent to finishing the application, as without the controller's companion there is nothing more you can do.

Let's run the code now.
"""
import tkinter

skylight = tkinter.Tk()
skylight.mainloop()
