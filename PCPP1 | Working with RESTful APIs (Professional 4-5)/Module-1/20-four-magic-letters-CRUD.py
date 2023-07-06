"""
Now we’re going to switch letters and make R our current hero. We'll show you how to delete a car from our offer.

As you already know, this is done by using the DELETE method, which is covered by the delete() function. Moreover, we'll do something more – we’ll divide our action into two stages:

1. we'll ask the server to delete one car of a specified id knowing that the server will keep the connection alive;

2. we’ll ask the server to present the current contents of the offer while suggesting that the connection should be closed immediately after the transmission.

Analyze the code in the editor:

Line 37: we prepare our own request header which will supplement the default one that is silently being sent along with each request – it's a dictionary with the key Connection (this is the same name as the one sent by the server) and the value set to Close; we’ll send it to the server soon;

Line 39: we make use of delete() – note the URI which describes the item to delete;

Line 40: we print the server's status code;

Line 41: we ask the server to show us the complete car list, but we also send our request to close the connection – this is done by setting a parameter named headers;

Line 46: we'd like to check if the server has honored our recommendation.

And this is our output:
res=200
Connection=close
id        | brand          | model     | production_year     | convertible    |
2         | Chevrolet      | Camaro    | 1988                | True           |
3         | Aston Martin   | Rapide    | 2010                | False          |
4         | Maserati       | Mexico    | 1970                | False          |
5         | Nissan         | Fairlady  | 1974                | False          |
6         | Mercedes Benz  | 300SL     | 1957                | True           |

output

As you can see, the deletion was successful (there is no car with id 1 in the list), the server responded with 200 (“okay”) and complied with our request.
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


headers = {'Connection': 'Close'}
try:
    reply = requests.delete('http://localhost:3000/cars/1')
    print("res=" + str(reply.status_code))
    reply = requests.get('http://localhost:3000/cars/', headers=headers)
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
