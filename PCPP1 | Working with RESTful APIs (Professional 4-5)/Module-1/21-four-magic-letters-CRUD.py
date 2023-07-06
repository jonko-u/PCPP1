"""
Let's add a new car to our offer. It means that now we’ll invite the letter C onto the stage. Adding a new item means that we’ll have to send the item to the server. Be careful, as this will require some additional steps.

The new steps are encoded in line 1, and lines 21 through 53:

Line 1: we add json to the import list – we’ll need it to make a textual representation of the new item/car;

Line 39: if we’re going to send anything to the server, the server must be aware of what it actually is; as you already know, the server informs us about the type of the contents using the Content-Type field; we can use the same technique to warn the server that we’re sending something more than a bare request. This is why we prepare our Content-Type field with the appropriate value;

Line 40: look! This is our new car! We prepared all the data needed and packed it inside a Python dictionary – of course, we'll convert it into JSON before we send it out into the world;

Line 45: we want to check how the resulting JSON message looks – prevention is better than a cure;

Line 47: this is where the most important things happen – we invoke the post() function (note the URI – it just points to the resource, not the particular item) and set two additional parameters: one (headers) to complement the request header with the Content-Type field, and the second (data) to pass the JSON message to the request.

Keep your fingers crossed as we’re going to run it now.

This is the output:
{"id": 7,"brand":"Porsche","model":"911","production_year":1963,"convertible":false}
reply=201
Connection=close
id        | brand          | model     | production_year     | convertible    |
2         | Chevrolet      | Camaro    | 1988                | True           |
3         | Aston Martin   | Rapide    | 2010                | False          |
4         | Maserati       | Mexico    | 1970                | False          |
5         | Nissan         | Fairlady  | 1974                | False          |
6         | Mercedes Benz  | 300SL     | 1957                | True           |
7         | Porsche        | 911       | 1963                | False          |

output

Wow! It worked! What a joy! Note the server's status code – it's 201 ("created").
"""
import json
import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


h_close = {'Connection': 'Close'}
h_content = {'Content-Type': 'application/json'}
new_car = {'id': 7,
           'brand': 'Porsche',
           'model': '911',
           'production_year': 1963,
           'convertible': False}
print(json.dumps(new_car))
try:
    reply = requests.post('http://localhost:3000/cars', headers=h_content, data=json.dumps(new_car))
    print("reply=" + str(reply.status_code))
    reply = requests.get('http://localhost:3000/cars/', headers=h_close)
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')
