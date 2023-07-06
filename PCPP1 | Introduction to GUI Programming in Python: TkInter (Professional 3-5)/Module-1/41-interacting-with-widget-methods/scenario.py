"""
The observer should be declared as a three-parameter function:

def observer(id, ix, act):
:
:

    id – an internal observable variable identifier (unusable for us);
    ix – an empty string (always – don’t ask us why, it’s tkinter’s business)
    act – a string informing us what happened to the variable or, in other words, what reason triggered the observer ('r', 'w' or 'u')

If you don’t need any of the arguments, you can declare the observer as: def obs(*):

Removing the observer is done with a method named trace_vdelete():

variable.trace_vdelete(trace_mode,obsid)

Its arguments’ meanings are as follows:

    trace_mode – the mode in which the observer has been created;
    obsid – the observer’s identifier obtained from the previous trace() invocation.


We’ve prepared a simple snippet showing how the observable variables cooperate with their observers. Take a look at it, we've provided it in the editor.

The code creates one observable variable of type StringVar and assigns two observers to it – one for reading and one for writing. The observers send a line to stdout when invoked.

Trace the code’s execution and try to explain its behavior. We’re sure you can do it.
"""
import tkinter as tk


def r_observer(*args):
    print("Reading")


def w_observer(*args):
    print("Writing")


dummy = tk.Tk()    # we need this although we won't display any windows
variable = tk.StringVar()
variable.set("abc")
r_obsid = variable.trace("r", r_observer)
w_obsid = variable.trace("w", w_observer)
variable.set(variable.get() + 'd')  # read followed by write
variable.trace_vdelete("r", r_obsid)
variable.set(variable.get() + 'e')
variable.trace_vdelete("w", w_obsid)
variable.set(variable.get() + 'f')
print(variable.get())
