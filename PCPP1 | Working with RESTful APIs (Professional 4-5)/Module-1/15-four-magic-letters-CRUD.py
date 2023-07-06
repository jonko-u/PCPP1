"""
Reading raw JSON messages isn't a lot of fun. To be honest, it's not fun at all. Let's make things a bit more fun, and write some uncomplicated code to present server responses in an elegant and clear way.

Look at the code in the editor. This is our attempt at this ambitious challenge.

Let's analyze it:

    Line 3: we've collected all the properties' names in one place – we’ll use them to perform look-ups through JSON data and to print a beautiful header line over the table;
    Line 4: these are the widths occupied by the properties;
    Line 7: we’ll use this function to print the table's header;
    Line 8: we iterate through key_names and key_widths coupled together by the zip() function;
    Line 9: we print each property's name expanded to the desired length and put a bar at the end;
    Line 10: it's time to complete the header line;
    Line 13: we’ll use this function to print one line filled with each car's data;
    Line 14: the iteration is exactly the same as in showhead(), but...
    Line 15: ...we print the selected property value instead of the column title;
    Line 19: we’ll use this function to print the contents of the JSON message as a list of items;
    Line 20: we’re going to present the user with a charming table with a header...
    Line 21 and 19: ...and a dataset of all the cars from the list, one car per line;
    Line 31: we make use of our brand new code here.

The output looks as follows now:
id        | brand          | model     | production_year     | convertible    |
1         | Ford           | Mustang   | 1972                | False          |
2         | Chevrolet      | Camaro    | 1988                | True           |
3         | Aston Martin   | Rapide    | 2010                | False          |
4         | Maserati       | Mexico    | 1970                | False          |
5         | Nissan         | Fairlady  | 1974                | False          |
6         | Mercedes Benz  | 300SL     | 1957                | True           |

output

"""
import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    for car in json:
        show_car(car)


try:
    reply = requests.get('http://localhost:3000/cars')
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    else:
        print('Server error')
