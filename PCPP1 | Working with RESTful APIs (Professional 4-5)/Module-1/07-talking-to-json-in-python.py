"""
As you can see, Python uses a small set of simple rules to build JSON messages from its native data. Here it is:

Table of JSON elements


It looks simple and consistent. So where’s the trap?

The trap is here:

import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


some_man = Who('John Doe', 42)
print(json.dumps(some_man))

The output you'll see is extremely disappointing:
TypeError: Object of type 'Class' is not JSON serializable

output

Yes, that's the clue. You cannot just dump the content of an object, even an object as simple as this one.

Of course, if you don't need anything more than a set of object properties and their values, you can perform a (somewhat dirty) trick and dump not the object itself, but its __dict__ property content. It will work, but we expect more.

What should we do?

There are at least two options we can make use of. The first of them is based on the fact that we can substitute the function dumps() uses to obtain a textual representation of its argument. There are two steps to take:

    write your own function knowing how to handle your objects;
    make dumps() aware of it by setting the keyword argument named default;

Now look at the code in the editor window. The example shows a simple implementation of the idea.

The code prints:
{"name": "John Doe", "age": 42}

output

Note: we decided to use the dictionary as a target for the JSON message. Thanks to that we’ll save the property names along with their values. It’ll make JSON easier to read and more understandable for humans.

Note: raising a TypeError exception is obligatory – this is the only way to inform dumps() that your function isn't able to convert objects other than those derived from the class Who.

Note: the process in which an object (stored internally by Python) is converted into textual or any other portable aspect is often called serialization. Similarly, the reverse action (from portable into internal) is called deserialization.

As you can see, we’ve converted (serialize) our object into a dictionary – dumps() will turn it into a JSON object.
"""
import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')


some_man = Who('John Doe', 42)
print(json.dumps(some_man, default=encode_who))
