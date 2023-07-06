"""
As previously, a purer object approach is also possible, and is based on redefining the JSONDecoder class. Unfortunately, this variant is more complicated than its encoding counterpart.

We don't need to rewrite any method, but we do have to redefine the superclass constructor, which makes our job a little more painstaking. The new constructor is intended to do just one trick – set a function for object creation.

As you can see, this is exactly the same thing we did before, but expressed at a different level.

We're glad to inform you that we’ve now gathered enough knowledge to move on to the next level. We’re going to return to some network issues, but we also want to show you some handy new tools.
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
            return super().default(self)


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)


some_man = Who('Jane Doe', 23)
json_str = json.dumps(some_man, cls=MyEncoder)
new_man = json.loads(json_str, cls=MyDecoder)

print(type(new_man))
print(new_man.__dict__)
