"""
The last remaining letter is U, so now we'll update one of the existing items. Updating an item is actually similar to adding one.

Take a look at the code in the editor. Let's analyze it.

Line 33: the header is the same as previously, as we'll send json to the server;

Lines 34 through 38: this is the new data for the item with id equal to 6; note – we've updated the production year (it should be 1967 instead of 1957)

Line 40: now we invoke the put() function; note – we have to make a URI that clearly indicates the item being modified; moreover, we must send the complete item, not only the changed property.

And this is what we see on the screen:
reply=200
Connection=close
id        | brand          | model     | production_year     | convertible    |
2         | Chevrolet      | Camaro    | 1988                | True           |
3         | Aston Martin   | Rapide    | 2010                | False          |
4         | Maserati       | Mexico    | 1970                | False          |
5         | Nissan         | Fairlady  | 1974                | False          |
6         | Mercedes Benz  | 300SL     | 1967                | True           |
7         | Porsche        | 911       | 1963                | False          |

output

Congratulations! The update was fully successful!

Moreover, we’ve completed our trip through the lands of CRUD and REST. It was a long but very satisfactory journey.
"""
import requests, json

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
car = {'id': 6,
       'brand': 'Mercedes Benz',
       'model': '300SL',
       'production_year': 1967,
       'convertible': True}
try:
    reply = requests.put('http://localhost:3000/cars/6', headers=h_content, data=json.dumps(car))
    print("res=" + str(reply.status_code))
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