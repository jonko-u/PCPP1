"""
If you don't need all the contents of the resource, you can prepare a specific GET request which requires only one item and uses id as a key. A URI looks like this then:

http://server:port/resource/id

We’re going to test it now but our code needs some improvement to behave properly – look at the code in the editor. Let's analyze it:

Lines 26 through 34: we must be prepared for the fact that the server won't send a list of items if we ask for one.

Lines 44 through 45: if there is no item of the requested id, the server will set the status code to 404 (“not found”) – this is how we handle this issue.

Note the URI we used there.

The program prints:
id        | brand          | model     | production_year     | convertible    |
2         | Chevrolet      | Camaro    | 1988                | True           |

output

Try to change the id and test the program's behavior.
"""
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


try:
    reply = requests.get('http://localhost:3000/cars/2')
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')