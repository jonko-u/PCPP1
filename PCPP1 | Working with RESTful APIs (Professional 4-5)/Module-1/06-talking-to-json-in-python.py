"""Working with the JSON module in Python

Now that we're familiar with JSON essentials, it's time to learn how to use it with Python. We're a little worried you may think that we want you to laboriously build JSON messages, fretting over all these brackets, parentheses and colons, and to break down complex JSON lines into prime factors. Nothing could be further from the truth! We’re not in the habit of coming up with such crazy ideas, although, to be honest, it's not as complex as it may seem and we're convinced that you’d be able to cope with such a challenge. Fortunately, you don't need to.

Why?

Because there’s a Python module – named JSON – which is able to perform all those drudgeries for you.

How do we start a new adventure? It's obvious, and we're sure that you knew it before we asked:

import json


The first JSON module's power is the ability to automatically convert Python data (not all of it and not always) into a JSON string. If you want to carry out such an operation, you may use a function named dumps().

Note: the ’s at the end of the function's name means string. There is a very similar function with the name deprived of this suffix which writes the JSON string to the file for file-like streams.

The function does what it promises – it takes data (even somewhat complicated data) and produces a string filled with a JSON message. Of course, dumps() isn't a prophet and it's not able to read your mind, so don't expect miracles.

Let’s start with some simple snippets.

The first of our samples takes a number and outputs a number – we don't expect anything more:

import json

electron = 1.602176620898E10−19
print(json.dumps(electron))

The code outputs:
16021766189.98

output

Note: the notation is different but the value remains the same. Check it yourself.
"""
import json
# list
my_list = [1, 2.34, True, "False", None, ['a', 0]]
print(json.dumps(my_list))
# dict
my_dict = {'me': "Python", 'pi': 3.141592653589, 'data': (1, 2, 4, 8), 'set': None}
print(json.dumps(my_dict))
