"""
There are two remaining widgets we want to tell you about – the first one is just a widget, while the second is, in fact, a set of cooperating widgets.

The Entry widget not only presents a line of text, but is also able to edit the text according to the user’s actions. Using an Entry is necessary when you are going to ask the user for any textual information: name, password, email, etc. The widget implements all standard edit operations like inserting, removing, scrolling, selecting, copying and pasting, etc..

We’ll show you only the basic possibilities of the widget, as it’s full equipment is extremely complex. Fortunately, we don’t need its entire flexibility when we just want to enter and validate a line of text.

Here are some of Entry’s properties:
Entry property 	Property meaning
command 	although Entry is obviously a clickable widget, it doesn’t allow you to bind a callback through the command property. You can observe and control all occurring changes instead by setting the tracer function for the observable variable which cooperates with Entry (we’ll show you this – be patient!)
show 	a string assigned to this property will be displayed instead of the actual characters entered into the input field; e.g., if you set show='*', this will enable the widget to safely edit the user’s password
state 	the same as for Button
textvariable 	an observable StringVar reflecting the current state of the input field
width 	the input field’s width (in characters)

And now, some of Entry’s methods:
Entry method 	Method role
get() 	returns the current input field’s contents as a string
set(s) 	sets the whole input field’s contents with the s string
delete(first, last=None) 	deletes a part of the input field’s contents; first and last can be integers with values indexing the string; if the last argument is omitted, a single character is deleted; if last is specified as END, it points to the place after the last field’s character
insert(index, s) 	inserts the s string at the field position pointed to by index

Our sample program in the editor shows you how to use an observable variable along with the trace callback (tracer) to force a user to enter only digits – all other characters will be silently ignored.

The tracer is invoked each time the input field is modified. The tracer remembers its previous state (using the last_s variable) and restores the field to this state if its current contents are invalid.

Note: we’ve had to use the focus_set() method, as the widget doesn’t take the focus itself.

Run the code and test its behavior.

Try to modify the code to allow the user to enter not more than five digits.
"""
import tkinter as tk


def digits_only(*args):
    global last_string
    string = text.get()
    if string == '' or string.isdigit():  # Field's content is valid.
        last_string = string
    else:
        text.set(last_string)


last_string = ''
window = tk.Tk()
text = tk.StringVar()
entry = tk.Entry(window, textvariable=text)
text.set(last_string)
text.trace('w', digits_only)
entry.pack()
entry.focus_set()
window.mainloop()
