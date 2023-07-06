"""
Objectives

Learn how to:

    use the socket module and its basic functionalities;
    manage simple http connections.

Scenario

We want you to write a simple CLI (Command Line Interface) tool which can be used in order to diagnose the current status of a particular http server. The tool should accept one or two command line arguments:

    (obligatory) the address (IP or qualified domain name) of the server to be diagnosed (the diagnosis will be extremely simple, we just want to know if the server is dead or alive)
    (optional) the server's port number (any absence of the argument means that the tool should use port 80)
    use the HEAD method instead of GET — it forces the server to send the full response header but without any content; it's enough to check if the server is working properly; the rest of the request remains the same as for GET.

We also assume that:

    the tool checks if it is invoked properly, and when the invocation lacks any arguments, the tool prints an error message and returns an exit code equal to 1;
    if there are two arguments in the invocation line and the second one is not an integer number in the range 1..65535, the tool prints an error message and returns an exit code equal to 2;
    if the tool experiences a timeout during connection, an error message is printed and 3 is returned as the exit code;
    if the connection fails due to any other reason, an error message appears and 4 is returned as the exit code;
    if the connection succeeds, the very first line of the server’s response is printed.

Hints:

    to access command line arguments, use the argv variable from the sys module; its length is always one more than the actual number of arguments, as argv[0] stores your script's name; this means that the first argument is at argv[1] and the second at argv[2]; don't forget that the command line arguments are always strings!
    returning an exit code equal to n can be achieved by invoking the exit(n) function.

Assuming that the tool is placed in a source file name sitechecker.py, here are some real-use cases:
"""
import logging
import socket
import sys

class ServerChecker:
    def __init__(self, address, port=80):
        self.address = address
        self.port = port

    def check_status(self):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # Set a timeout of 5 seconds for the connection

        # Connect to the server
        try:
            sock.connect((self.address, self.port))
        except socket.timeout:
            logging.error("Connection timed out.")
            return 3, None
        except (socket.gaierror, ConnectionRefusedError):
            logging.error("Unable to connect to the server.")
            return 4, None

        # Send a HEAD request to the server
        try:
            request = f"HEAD / HTTP/1.1\r\nHost: {self.address}\r\nConnection: close\r\n\r\n".encode()
            sock.sendall(request)
            response = sock.recv(1024).decode()
        except socket.timeout:
            logging.error("Connection timed out.")
            return 3, None
        except:
            logging.error("Unable to communicate with the server.")
            return 4, None

        # Check the response status code
        status_code = response.split()[1]
        if status_code == "200":
            logging.info("Server is up and running.")
        elif status_code == "301":
            logging.error("Resource has been permanently moved to: %s", response.partition("Location: ")[2].split("\r\n")[0])
            return 5, status_code
        elif status_code == "302":
            logging.warning("Resource has been temporarily moved to: %s", response.partition("Location: ")[2].split("\r\n")[0])
            return 6, status_code
        elif status_code == "400":
            logging.error("Bad Request: %s", response)
            return 8, status_code
        elif status_code == "401":
            logging.error("Unauthorized: %s", response)
            return 9, status_code
        elif status_code == "402":
            logging.error("Payment Required: %s", response)
            return 10, status_code
        elif status_code == "403":
            logging.error("Forbidden: %s", response)
            return 11, status_code
        elif status_code == "404":
            logging.error("Not Found: %s", response)
            return 12, status_code
        elif status_code == "500":
            logging.error("Internal Server Error: %s", response)
            return 13, status_code
        elif status_code == "502":
            logging.error("Bad Gateway: %s", response)
            return 14, status_code
        elif status_code == "503":
            logging.error("Service Unavailable: %s", response)
            return 15, status_code
        else:
            logging.error("Server returned status code %s", status_code)
            return 7, status_code

        # Close the socket connection
        sock.close()

        return 0, status_code
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <server_address>")
        sys.exit(1)

    server_address = sys.argv[1]

    # Perform server check
    checker = ServerChecker(server_address)
    exit_code, status_code = checker.check_status()

    # Log result
    if status_code is not None:
        logging.info("Server returned status code %s", status_code)
    if exit_code == 0:
        logging.info("Server check succeeded")
    else:
        logging.error("Server check failed with exit code %s", exit_code)