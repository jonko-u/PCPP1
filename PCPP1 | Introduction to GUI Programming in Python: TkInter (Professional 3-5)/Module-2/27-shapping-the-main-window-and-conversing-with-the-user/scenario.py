"""
Usually, when you want to announce something to the user or to ask any simple question (e.g., yes/no), you don’t need to create your own means – you can use one of the predefined functions gathered within the messagebox module. We showed you some of its possibilities before, but now we want to summarize the issue and to present all of the most useful tools.

All these functions display a modal dialog window and wait for a user response. The dialog’s behavior is determined by three parameters:

    title – a string displayed in the dialog’s title bar (it can’t be very long, of course);
    message – a string displayed inside the dialog; note: the \n plays its normal role and breaks up the message’s lines;
    options – a set of options shaping the dialog in a non-default way, two of which are useful to us:
        default – sets the default (pre-focused) answer; usually, it’s focused on the button located first from the left; this can be changed by setting the keyword argument with identifiers like CANCEL, IGNORE, OK, NO, RETRY, and YES;
        icon – sets the non-default icon for the dialog: possible values are: ERROR, INFO, QUESTION, and WARNING.

The first of the functions we’re going to show you is askyesno(), designed to get yes/no user responses. The function creates a dialog which:

    contains an icon with a question mark in it;
    returns True if the user’s response is Yes and False otherwise (e.g., when the user closes the dialog using its close button)

In the editor we've provided a simple sample code showing the function in action. Note: the code outputs its messages to the console. Don’t overlook them.
"""
import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.askyesno("?", "To be or not to be?")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="Ask the question!", command=question)
button.pack()
window.mainloop()
