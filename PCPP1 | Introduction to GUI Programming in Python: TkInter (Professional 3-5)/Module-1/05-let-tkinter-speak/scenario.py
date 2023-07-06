"""
Of course, closing the window without asking the user if they are really sure that this is exactly what they want to do isn't a good way to build up a relationship with them.

We definitely want to ask the user before we permanently remove their window from sight.

Fortunately, tkinter is very helpful with this issue. There is a module named messagebox (the name speaks for itself) which is your great companion in this and similar matters.

messagebox is able to create dialog boxes intended to ask questions, display messages, and to receive a user's reply.

The dialog box is an example of a modal window – a window which grabs the whole of the application's focus. It means that all other application widgets become deaf as long as the modal window is present.

We've provided the amended code in the editor window.

Let's dive into our new code.

    we've had to add a second import directive – as messagebox is a module located inside the tkinter package, we need to use the from variant of the import;
    the essence of our modification is hidden inside the callback:
        we invoke the askquestion() function by passing two arguments to it: the first will be used as a dialog window title, the second will be displayed inside the window to make the user aware of the incoming issue;
        the askquestion() function returns a string which is equal to yes if the user has clicked the confirming button (note: the text on the button depends of the OS international settings, and will be set to the word yes or its local analog)

As you can see, the mechanism is easy and handy. Let's run the code and check its results. We hope that you see something like this:

Of course, our code is very disappointing. For example, the window can be closed instantly, without any question, when the user clicks the closing button. This is not very elegant; you'll probably agree with that.

We ask you for forgiveness – this is only an example, obviously too simple to be utilized in regular conditions, but it gives us a good starting point from which to continue the journey into more complex tkinter facilities.

Stay tuned!

"""
import tkinter
from tkinter import messagebox


def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        skylight.destroy()


skylight = tkinter.Tk()
skylight.title("Skylight")
button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)
skylight.mainloop()
