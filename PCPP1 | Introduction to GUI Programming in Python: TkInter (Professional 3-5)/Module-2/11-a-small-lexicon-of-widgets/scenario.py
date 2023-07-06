"""
Look at the code below. We’ve made two changes – we’ve added two underlined property specifications to the Menu() invocations:

    at line 15: underline=0 (sets Alt-F as a hotkey)
    at line 18: underline=1 (sets Alt-B as a hotkey)

Check if it works – we hope it does.
12.07.png

Note: you’re obliged to ensure that all hotkeys are unique!

"""
import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")


window = tk.Tk()

main_menu = tk.Menu(window)
window.config(menu=main_menu)
sub_menu_file = tk.Menu(main_menu)
# setting the hotkey to "Alt-F"
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
sub_menu_help = tk.Menu(main_menu)
# setting the hotkey to "Alt-B"
main_menu.add_command(label="About...", command=about_app, underline=1)

window.mainloop()
