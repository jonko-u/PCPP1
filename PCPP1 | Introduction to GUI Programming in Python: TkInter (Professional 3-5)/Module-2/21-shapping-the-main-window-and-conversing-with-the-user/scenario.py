"""
Changing the main window’s icon is more troublesome if you want to do in a portable way. Here’s one working solution, although we agree it’s not very elegant.

Take a look at the code we've provided in the editor.

The key to success is line #5 – it directly invokes one of the tkinter internal, low-level mechanisms directly communicating with the OS’s window manager. The call asks the OS to exchange the window’s icon with the one provided by you. The icon is transferred by the last method’s argument, but if you want this to work successfully, you have to:

    prepare an icon as a PNG image;
    put the image in the same directory where the application resides;
    use a PhotoImage class constructor to convert the PNG file into an internal tkinter representation (PhotoImage() is a part of tkinter, and we’re going to tell you more about it soon)

13.02.png

Note: we’ve used the Python Institute’s logo as the application icon (logo.png). Feel free to replace it with whatever you choose.

"""
import tkinter as tk

window = tk.Tk()
window.title('Icon?')
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='logo.png'))
window.bind("&lt;Button-1&gt;", lambda e: window.destroy())
window.mainloop()
