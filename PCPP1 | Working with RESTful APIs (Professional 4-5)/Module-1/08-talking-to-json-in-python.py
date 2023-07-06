"""
The second approach is based on the fact that the serialization is actually done by the method named default(), which is a part of the json.JSONEncoder class. It gives you the opportunity to overload the method defining a JSONEncoder's subclass and to pass it into dumps() using the keyword argument named cls – just like in the code we've provided in the editor.

As you can see, we are released from the obligation to raise any exceptions. Nice, isn't it?

The code produces the same output as the previous one:
{"name": "John Doe", "age": 42}

output

It seems that we know enough about how to travel from Python land to JSON world, but still know anything about how to return. Let's take care of it.

The function which is able to get a JSON string and to turn it into Python data is named loads() – it takes a string (hence the s at the end of its name) and tries to create a Python entity corresponding to the received data.

This is how it goes:

import json

jstr = '16021766189.98'
electron = json.loads(jstr)
print(type(electron))
print(electron)

The code prints:
<class 'float'>
16021766189.98

output

The loads() function is able to cope with strings, too. Take a look at the snippet:

import json

jstr = '"\\"The Meaning of Life\\" by Monty Python\'s Flying Circus"'
comics = json.loads(jstr)
print(type(comics))
print(comics)

Can you see the double backslashes inside the jstr? Are they really needed?

Yes, they are, as we have to deliver an exact JSON string into the loads(). This means that the backslash must precede all quotes existing within the string. Removing any of them will make the string invalid and loads() will not like it for sure.

The code outputs:
<class 'str'>
"The Meaning of Life" by Monty Python's Flying Circus
"""
import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, z)


some_man = Who('John Doe', 42)
print(json.dumps(some_man, cls=MyEncoder))
