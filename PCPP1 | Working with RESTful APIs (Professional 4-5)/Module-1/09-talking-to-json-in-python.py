"""


And what about lists? Is loads() smart enough to interpret them correctly?

Yes, it is – take a look:

import json

jstr = '[1, 2.34, true, "False", null, ["a", 0]]'
my_list = json.loads(jstr)
print(type(mylist))
print(mylist)

The code prints:
<class 'list'>
[1, 2.34, True, 'False', None, ['a', 0]]

output

We expect that the JSON object will be processed correctly.

Yes, it will:

import json

json_str = '{"me":"Python","pi":3.141592653589, "data":[1,2,4,8],"friend":"JSON","set": null}'
my_dict = json.loads(json_str)
print(type(my_dict))
print(my_dict)

The code prints:
<class 'dict'>
{'me': 'Python', 'pi': 3.141592653589, 'data': [1, 2, 4, 8], 'friend': 'JSON', 'set': None}

output

Our tests show that the table we presented before works successfully in both directions. There’s only one specific difference: if a number encoded inside a JSON string doesn't have any fraction part, Python will create an integer number, or a float number otherwise.

But what about Python's objects – can we deserialize them in the same way as we performed the serialization?

As you probably expect, deserializing an object may require some additional steps. Yes, indeed. As loads() isn't able to guess what object (of which class) you actually need to deserialize, you have to provide this information.

Take a look at the snippet we've provided in the editor window.

As you can see, there’s a keyword argument name object_hook, which is used to point to the function responsible for creating a brand new object of a needed class and for filling it with actual data.

Note: the decode_who() function receives a Python entity, or more specifically – a dictionary. As Who's constructor expects two ordinary values, a string and a number, not a dictionary, we have to use a little trick – we've employed the double * operator to turn the directory into a list of keyword arguments built out of the dictionary's key:value pairs. Of course, the keys in the dictionary must have the same names as the constructor's parameters.

Note: the function, specified by the object_hook will be invoked only when the JSON string describes a JSON object. Sorry, there are no exceptions to this rule.
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
        raise TypeError(w.__class__.__name__ + 'is not JSON serializable')


def decode_who(w):
    return Who(w['name'], w['age'])


old_man = Who("Jane Doe", 23)
json_str = json.dumps(old_man, default=encode_who)
new_man = json.loads(json_str, object_hook=decode_who)
print(type(new_man))
print(new_man.__dict__)
