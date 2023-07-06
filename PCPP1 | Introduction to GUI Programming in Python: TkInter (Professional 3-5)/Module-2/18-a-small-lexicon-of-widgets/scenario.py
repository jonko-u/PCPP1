"""
If you want some of the (sub)menu items to be accessible through a dedicated hot-key, you have to perform two steps:

    set the item’s property named accelerator with a string naming the hot-key (note: this has no other effect than just displaying the right-aligned string inside the item – no callback is set at the moment)
    make a global binding linking the hot-key with a proper callback.

12.14.png

Look – we’ve applied these steps to our code making Ctrl-Q a shortcut designed to close the application – it happens in lines #9 (we modified the AreYouSure() function header), #33 (we added the accelerator property) and #38 (global binding to <Control-q>).
"""
import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")


def are_you_sure(event=None):
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        window.destroy()


def open_file():
    messagebox.showinfo("Open doc", "We'll open a file here...")


window = tk.Tk()

main_menu = tk.Menu(window)
window.config(menu=main_menu)
sub_menu_file = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)

for i in range(8):
    number = str(i + 1)
    sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)

sub_menu_file.add_separator()
sub_menu_file.add_command(label="Quit", accelerator="Ctrl-Q",
                          underline=0, command=are_you_sure)
sub_menu_help = tk.Menu(main_menu)
main_menu.add_command(label="About...", command=about_app, underline=1)

window.bind_all("<Control-q>", are_you_sure)
window.mainloop()
