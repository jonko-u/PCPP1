"""


    Logo

    1.7.1.2 Four magic letters: CRUD

Module (82%)
Section (17%)

    List of contents
    Working with RESTful APIs -- Study Resources Now
        Back
        Working with RESTful APIs -- Study Resources
        1.1.1 Basic concepts of network programming
            Back
            1.1.1 Basic concepts of network programming
            1.1.1.1 Python Professional Course Series: RESTful APIs
            1.1.1.2 Networks, layers and the Internet: introduction
            1.1.1.3 Network sockets - a basic means of network programming
            1.1.1.4 Domains, addresses, ports, protocols and services
            1.1.1.5 Domains, addresses, ports, protocols and services
            1.1.1.6 Clients and servers - two sides of network communication
        1.2.1 How to use sockets in Python?
            Back
            1.2.1 How to use sockets in Python?
            1.2.1.1 How to use sockets in Python
            1.2.1.2 How to create a socket in Python
            1.2.1.3 How to connect to a server
            1.2.1.4 How to say something in HTTP
            1.2.1.5 How to request a document from a server
            1.2.1.6 How to request a document from a server
            1.2.1.7 How to close the connection
            1.2.1.8 Complete HTTP client
            1.2.1.9 The server's response
            1.2.1.10 When something goes wrong... - exceptions
        1.3.1 Introduction to JSON
            Back
            1.3.1 Introduction to JSON
            1.3.1.1 JSON – our new friend
            1.3.1.2 JSON – our new friend
            1.3.1.3 JSON – our new friend
            1.3.1.4 JSON – our new friend
            1.3.1.5 JSON – our new friend
        1.4.1 Using the json module in Python
            Back
            1.4.1 Using the json module in Python
            1.4.1.1 Talking to JSON in Python
            1.4.1.2 Talking to JSON in Python
            1.4.1.3 Talking to JSON in Python
            1.4.1.4 Talking to JSON in Python
            1.4.1.5 Talking to JSON in Python
        1.5.1 Introduction to XML -- Why do we prefer to use JSON?
            Back
            1.5.1 Introduction to XML -- Why do we prefer to use JSON?
            1.5.1.1 What is XML and why do we prefer to use JSON?
            1.5.1.2 What is XML and why do we prefer to use JSON?
            1.5.1.3 What is XML and why do we prefer to use JSON?
            1.5.1.4 What is XML and why do we prefer to use JSON?
            1.5.1.5 What is XML and why do we prefer to use JSON?
            1.5.1.6 What is XML and why do we prefer to use JSON?
            1.5.1.7 What is XML and why do we prefer to use JSON?
            1.5.1.8 What is XML and why do we prefer to use JSON?
        1.6.1 HTTP made simple –- the request module
            Back
            1.6.1 HTTP made simple –- the request module
            1.6.1.1 Making life easier with the requests module
            1.6.1.2 Making life easier with the requests module
            1.6.1.3 Making life easier with the requests module
            1.6.1.4 Making life easier with the requests module
            1.6.1.5 Making life easier with the requests module
            1.6.1.6 Making life easier with the requests module
            1.6.1.7 Making life easier with the requests module
            1.6.1.8 Making life easier with the requests module
            1.6.1.9 Making life easier with the requests module
            1.6.1.10 Making life easier with the requests module
        1.7.1 CRUD -- how to build a simple REST client? Now
            Back
            1.7.1 CRUD -- how to build a simple REST client?
            1.7.1.1 Four magic letters: CRUD
            1.7.1.2 Four magic letters: CRUD Now
            1.7.1.3 Four magic letters: CRUD
            1.7.1.4 Four magic letters: CRUD
            1.7.1.5 Four magic letters: CRUD
            1.7.1.6 Four magic letters: CRUD
            1.7.1.7 Four magic letters: CRUD
            1.7.1.8 Four magic letters: CRUD
            1.7.1.9 Four magic letters: CRUD
            1.7.1.10 Four magic letters: CRUD
            1.7.1.11 Four magic letters: CRUD
            1.7.1.12 That's all, Folks!
    Labs
        Back
        Labs
        2.1.1 Python Professional Course Series: Lab & Assessment
            Back
            2.1.1 Python Professional Course Series: Lab & Assessment
            2.1.1.0 Python Professional Course Series: Lab & Assessment
            2.1.1.1 HTTP server availability checker Lab
            2.1.1.2 Vehicle data decoder/encoder Lab
            2.1.1.3 New York Stock Exchange Lab
            2.1.1.4 Server checker once again Lab
        2.2.1 Final Project
            Back
            2.2.1 Final Project
            2.2.1.1 PROJECT: Vintage cars database Lab
    Assessment
        Back
        Assessment
        3.1.1 Working with RESTful APIs | FINAL QUIZ Quiz
            Back
            3.1.1 Working with RESTful APIs | FINAL QUIZ
            3.1.1.1 Working with RESTful APIs | FINAL QUIZ Quiz
        3.2.1 Working with RESTful APIs | FINAL TEST Test
            Back
            3.2.1 Working with RESTful APIs | FINAL TEST
            3.2.1.1 Working with RESTful APIs | FINAL TEST Test

Now we’re ready to carry out some simple but instructive experiments with JSON. We’ll use it as an intermediate language to communicate with the HTTP server, implementing CRUD and storing a sample collection of data.

These are our assumptions:

    we'll make use of the previously presented json-server – we'll try to get it to work hard with all four letters making up CRUD;
    our initial database, processed on our demands by the json-server, will be a collection of retro cars written down in the cars.json file (Download cars.json zip file); the json-server will read the file in and will handle its contents according to our actions;
    each car is described by:
        id – a unique item number; note – each item in the collection must have the property of this name – this is how the server identifies each item and differentiates the items from each other;
        brand – a string;
        model – a string;
        production_year – an integer number;
        convertible – a Boolean value;
    the initial file contains data for six cars – don't be surprised if the server modifies its contents; if you want to reset the collection to the initial state, stop the server (use Ctrl-C for this purpose), replace the file with its original version (you can always download it from our site) and start the server again.

We’re ready to start now. Open the console, locate the directory where your cars.json is located and launch the server:

json-server --watch cars.json

Note (very important) – the fact that the json-server serves the data initially encoded as JSON has absolutely nothing to do with the fact that we will transmit JSON messages between the client (our code) and the server (json-server). The way the server is used to initialize and store data is actually a black-box for us (unless we are implementing the server itself). Different servers may use different means – it's none of our business when we are the clients.

CRUD + JSON = ∞


We'll start our journey with the letter R (read). We’ll try to convince the server to show us all the cars it offers.

Note: json-server assumes that the data collection inherits its name from the source data file name. As we named the file cars, the server will publish the data as cars, too. You have to use the name in the URI unless you want to get the default (root) document, which is completely useless to us.

Look at the code in the editor. It's very basic so far, but will grow soon – we promise:

    line 1: we import the requests module;
    line 3: we’re going to connect to the server inside the try block – this will allow us to protect ourselves against the possible effects of connection problems;
    line 4: we form the GET request and address it to the resource named cars located at the server working at the address specified as localhost, listening at port number 300;
    line 5: have we succeeded?
    line 6: unfortunately, we have failed; it seems that the server isn't working, or is inaccessible;
    line 8: good news – the server's responded! Let's check the status code;
    line 9: we print the data the server has sent us (rather boring); the response's contents are stored as a text property of the response object;
    line 11: bad news – the server likes neither us nor our request.

If everything goes well, we should see the full contents of the cars.json file printed on the screen. Of course, this is not a very special achievement, but now we’re sure that the server is ready to serve us, and we are ready to command it.

The HTTP server is able to transfer virtually any kind of data: text, image, video, sound, and many others. The question we have to face and to answer is: how do we recognize that we’ve actually got the JSON message?

Yes, of course, it’s obvious that we received what we expected, but it’s rather impossible to install “naked eye” into each piece of client code. Fortunately, there is a simpler way to resolve this issue. The server response's header contains a field named Content-Type. The field's value is analyzed by the requests module, and if its value announces JSON, a method named json() returns the string containing the received message.

We've modified the code a bit - look into the editor and analyze the lines:

Line 9: we print the Content-Type field's value;

Line 10: we print the text returned by the json() method.

This is what we've got:
application/json; charset=utf-8
[{'id': 1, 'brand': 'Ford', 'model': 'Mustang', 'production_year': 1972, 'convertible': False}, {'id': 2, 'brand': 'Chevrolet', 'model': 'Camaro', 'production_year': 1988, 'convertible': True}, {'id': 3, 'brand': 'Aston Martin', 'model': 'Rapide', 'production_year': 2010, 'convertible': False}, {'id': 4, 'brand': 'Maserati', 'model': 'Mexico', 'production_year': 1970, 'convertible': False}, {'id': 5, 'brand': 'Nissan', 'model': 'Fairlady', 'production_year': 1974, 'convertible': False}, {'id': 6, 'brand': 'Mercedes Benz', 'model': '300SL', 'production_year': 195 q7, 'convertible': True}]

output

Note the line starting with application/json – this is a premise used by the requests module to diagnose the response's contents.
"""
import requests

try:
    reply = requests.get("http://localhost:3000/cars")
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        print(reply.headers['Content-Type'])

        print(reply.text)
    else:
        print("Server error")
