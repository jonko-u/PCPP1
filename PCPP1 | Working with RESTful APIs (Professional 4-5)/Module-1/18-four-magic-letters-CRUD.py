"""
The json-server is also able to reverse the sort order – you just have to rewrite theURI in the following way:

http://server:port/resource?_sort=property&_order=desc

Note the & character – it separates additional request parameters from each other.

The amended code is in the editor.

And here's the output:
id        | brand          | model     | production_year     | convertible    |
3         | Aston Martin   | Rapide    | 2010                | False          |
2         | Chevrolet      | Camaro    | 1988                | True           |
5         | Nissan         | Fairlady  | 1974                | False          |
1         | Ford           | Mustang   | 1972                | False          |
4         | Maserati       | Mexico    | 1970                | False          |
6         | Mercedes Benz  | 300SL     | 1957                | True           |

output

Some servers can do much more, e.g., they can perform full-text searches, make slices, or analyze complex filtering expressions. The sky’s the limit.
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
    reply = requests.get('http://localhost:3000/cars?_sort=production_year&_order=desc')
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')
