"""


By default, a server implementing HTTP version 1.1 works in the following manner:

- it waits for the client's connection;

- it reads the client's request;

- it sends its response;

- it keeps the connection alive, waiting for the client's next request;

- if the client is inactive for some time, the server silently closes the connection; this means that the client is obliged to set up a new connection again if it wants to send another request.

The server informs the client whether the connection is kept or not by using a field named Connection, placed in the response's header.

Look at the code in the editor. Let's check it (note line 37).

The program prints:
Connection=keep-alive

output

close means that the server is going to close the connection as soon as the response is fully transmitted (this was the server’s default behavior in HTTP 1.0).

If the client knows that it won't bother the server with subsequent requests for some time, it may encourage the server to temporarily change its habits and close the connection immediately. It will conserve the server's resources.

How do we do that?
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
    reply = requests.get('http://localhost:3000/cars')
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