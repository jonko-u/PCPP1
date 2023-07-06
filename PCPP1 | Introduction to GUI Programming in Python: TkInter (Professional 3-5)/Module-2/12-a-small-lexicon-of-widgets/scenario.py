"""
Now we’ll extend the File submenu and add a Quit option to this.

The option’s action will be implemented by a simple callback giving the user the chance to change their mind.

We’ll use the add_command() method to achieve this goal.

This is what we get:
12.08.png

Check line #21 – this will tell you everything. Run the code.
"""
import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")


def are_you_sure():
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        window.destroy()


window = tk.Tk()

main_menu = tk.Menu(window)
window.config(menu=main_menu)
sub_menu_file = tk.Menu(main_menu)
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# add the QUIT action to the submenu
sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
sub_menu_help = tk.Menu(main_menu)
main_menu.add_command(label="About...", command=about_app, underline=1)

window.mainloop()
