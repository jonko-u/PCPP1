"""
Requesting a document from a server: continued

The recv() method (in our humble opinion, not a very fortunate abbreviation of receive) waits for the server's response, gets it, and puts it inside a newly created object of type bytes. Look at the code we've provided in the editor.

The argument specifies the maximal acceptable length of the data to be received. If the server's response is longer than this limit, it will remain unreceived.

You will need to invoke recv() again (maybe more than once) to get the remaining part of the data. It's a general practice to invoke recv() as long as it returns some data.

There are lots of bad things which can spoil our game. For example, the server may not want to talk with us.

The transmission may cause some errors, too. All these fatalities will raise exceptions.

What next?
"""
import socket

server_addr = input("What server do you want to connect to? ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_addr, 80))
sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")
reply = sock.recv(10000)