"""
A particular server may provide some additional facilities e.g., it may manipulate data before sending it to the client. The json-server is able to sort the items using any of the properties as a sort key (by default, it sorts items by their ids). Usually, the URI does the trick, but remember that there is no common standard covering such additional functions – consult the server's documentation to learn more.

The json-server assumes that a URI formed in the following way:

http://server:port/resource?_sort=property

causes the response to be sorted in ascending order using a property named prop. Note the ? character – it separates the resource identification from additional request parameters.

Let's try it. Look at the code in the editor (the lines we've changed: lines 37 through 47).

We've got the following output:

The output looks as follows now:
id        | brand          | model     | production_year     | convertible    |
6         | Mercedes Benz  | 300SL     | 1957                | True           |
4         | Maserati       | Mexico    | 1970                | False          |
1         | Ford           | Mustang   | 1972                | False          |
5         | Nissan         | Fairlady  | 1974                | False          |
2         | Chevrolet      | Camaro    | 1988                | True           |
3         | Aston Martin   | Rapide    | 2010                | False          |


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
    reply = requests.get('http://localhost:3000/cars?_sort=production_year')
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')