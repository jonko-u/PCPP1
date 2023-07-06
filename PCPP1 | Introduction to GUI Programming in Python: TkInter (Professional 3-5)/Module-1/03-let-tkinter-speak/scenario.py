"""
Now it's the turn of the button.

A button visible on the screen is, in fact, a reflection of an object of the Button class. To bring a button to life, you have to:

    create a Button class object (it'll be done by the class's constructor)
    place the button inside the main window (it'll be done by one of the window's methods)

Note the distinction: it can be said that the button creates itself, but to make it visible, you need the window's (not the button's!) method.

Take a look at the code in the editor window.

To create a Button class object, we make use of its constructor. Its first argument (which is a reference to the target window) is obligatory. All others are optional.

The one named text sets the initial button's title (note: the title can be changed at any time).

The object saved inside the button variable is now created, but still invisible. Moreover, the main window doesn't know where to put it within its interior. Let's fix that.

The act of placing the widget somewhere inside the window is done with a method named place(). As you can see, we use the method in a way in which the button's two coordinates are given: x and y. There are three important remarks that must be written here:

    the widget's coordinates refer defaultly to the pixel occupied by the upper-left corner;
    the widget's size is defaultly determined by the constructor in order to fit the widget's content (the title's length and height in this case)
    the widget's location is measured in pixels, but there is one important issue which distinguishes the screen coordinates from the ones used by the geometry; look: this is what the Cartesian two-dimensional coordinates system looks like:


    while the screen coordinates look as follows:



    This means that a pixel described as (x=10,y=10) is located near the top-left window corner. Be aware of this!

Now we're fully prepared to run the code.

Hi, Button! Nice to see you!



Can we click you? Of course we can. Does it change anything? No, it doesn't. Of course, the view of the button changes, simulating a real button's behaviors, but no other reactions can be seen. We don't like this.

And this is the moment when we should hire a new member onto our team – an event handler.

"""
import tkinter

skylight = tkinter.Tk()
skylight.title("Skylight")
button = tkinter.Button(skylight, text="Bye!")
button.place(x=10, y=10)
skylight.mainloop()