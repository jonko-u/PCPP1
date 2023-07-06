"""
Note: you cannot modify any of the (sub)menu item by using the standard config() method invocation, because from tkinter's point of view, the item is not a widget – it’s only a very specific widget component.

If you want to manipulate a menu’s item, you should use a dedicated method named entryconfigure(). The method accepts two parameters:

item.entryconfigure(i, prop=value)

    the first is an integer index of the modified item (entry)
    the second is a keyworded argument pointing to the modified property.

The snippet shows you how it works – it plays with the second entry’s state property – run the code, and observe its behavior:

12.15-1.png


Let’s gather together some of the menu’s properties and methods:
Property 	Property role
postcommand 	a callback invoked every time a menu’s item is activated
tearoff 	set to zero removes the tear-off decoration from the top of the cascade
state 	when set to DISABLED, the menu item is grayed and inaccessible; setting it to ACTIVE restores its normal functionality
accelerator 	a string describing a hot-key bound to the menu’s item
Method 	Method role
add_cascade(prop=val, ...) 	adds a cascade to the menu’s item
add_command(prop=val, ...) 	assigns an action to the menu’s item
add_separator() 	adds an separator line to the menu
entryconfigure(i, prop=val,...) 	modifies the i-th menu item’s property named prop

Now we’re going to show some ways of shaping the main window’s appearance.
"""
import tkinter as tk


def on_off():
    global accessible
    if accessible == tk.DISABLED:
        accessible = tk.ACTIVE
    else:
        accessible = tk.DISABLED
    sub_menu.entryconfigure(1, state=accessible)


accessible = tk.DISABLED
window = tk.Tk()
menu = tk.Menu(window)
window.config(menu=menu)
sub_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=sub_menu)
sub_menu.add_command(label="On/Off", command=on_off)
sub_menu.add_command(label="Switch", state=tk.DISABLED)
window.mainloop()
