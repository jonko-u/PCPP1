"""
Our steps are as follows:

    line 5: we define a simple callback which displays the About dialog;
    line 9: main window creation (nothing special at all)
    line 12: we create the main menu object...
    line 13: and embed it into the main window (note the way in which the config() method is used and which property we utilize to bind the menu)
    line 16: we create a submenu object (note the master window argument specification)
    line 17: we add the submenu to the main menu’s first item (note the add_cascade() method invocation)
    line 20: we create another submenu object…
    line 21: ...and bind a callback to it (note the add_command() method invocation)

Run the code and test it. Do you see that strange dashed line visible when you click the File main menu item?
12.06.png

Don’t worry, this it’s normal. We’ll deal with it soon.

A menu like this has one important disadvantage – it’s hard to use it without a mouse. Of course, you can use the Alt key to activate the menu and navigate through it using the cursor keys and Enter (you can test this), but we need something quicker and more convenient.
"""
import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")


window = tk.Tk()

# main menu creation
main_menu = tk.Menu(window)
window.config(menu=main_menu)

# 1st main menu item: an empty (as far) submenu
sub_menu_file = tk.Menu(main_menu)
main_menu.add_cascade(label="File", menu=sub_menu_file)

# 2nd main menu item: a simple callback
sub_menu_help = tk.Menu(main_menu)
main_menu.add_command(label="About...", command=about_app)

window.mainloop()
