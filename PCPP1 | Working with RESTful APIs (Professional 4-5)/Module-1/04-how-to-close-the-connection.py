"""
Closing the connection

As we want to neither send nor receive anything more, we ought to announce it to the server. We will do it in a very simple form, just like here:
import socket

server_addr = input("What server do you want to connect to? ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_addr, 80))
sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")
reply = sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)


Invoking shutdown() is like a message whispered directly into the server's ear: "We have no more to say to you. We don't want to hear from you, either. The rest is silence."

Thanks to that, the server is aware of our intentions.

The following function arguments say more about our views for the future:

    socket.SHUT_RD - we aren't going to read the server's messages anymore (we declare ourselves deaf)
    socket.SHUT_WR - we won't say a word (actually, we'll be dumb)
    socket.SHUT_RDWR - specifies the conjunction of the two previous options.

Is there anything more we should do now?

As our GET request demanded that the server close the connection as soon the response is sent and the server has been advised of our next steps (or rather of the fact that we've already done what we wanted to), we can assume that the connection is fully terminated at this moment.

Some would say that closing it explicitly is an exaggerated diligence. We don't share this view and prefer to close the connection by expressing it literally.

The parameterless close() method will do it for us - see our code in the editor.

Okay. We've received something. Is it worth seeing with our own eyes? We won't see until we see.
"""
import socket

server_addr = input("What server do you want to connect to? ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_addr, 80))
sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")
reply = sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)
sock.close()