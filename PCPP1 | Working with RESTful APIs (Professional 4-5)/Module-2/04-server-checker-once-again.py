"""
Objectives

Learn how to:

    use the requests module facilities;
    interpret server responses.

Scenario

Now we want to you to return to the issues discussed in lab #1. In fact, you need to implement exactly the same functionality as you embedded in your code previously, but this time you have to use the requests module instead of the socket module. Everything else should remain the same: the command line arguments and outputs have to be indistinguishable.

Hint: use the head() method instead of get(), as you don't need the whole root document the server sends to you — the header is enough to test whether or not the server is responding. Fortunately, head() has exactly the same interface as get(). Don't forget to handle all needed exceptions — don't leave your user without any clear explanations about anything that went wrong.
"""
import argparse
import logging
import requests

class ServerChecker:
    def __init__(self, url):
        self.url = url

    def check_status(self):
        try:
            response = requests.get(self.url, timeout=5, verify=True)
        except requests.exceptions.Timeout:
            logging.error("Connection timed out.")
            return 3, None
        except requests.exceptions.ConnectionError:
            logging.error("Unable to connect to the server.")
            return 4, None

        status_code = response.status_code
        if status_code == 200:
            logging.info("Server is up and running.")
        elif status_code == 301:
            logging.error("Resource has been permanently moved to: %s", response.headers['Location'])
            return 5, status_code
        elif status_code == 302:
            logging.warning("Resource has been temporarily moved to: %s", response.headers['Location'])
            return 6, status_code
        elif status_code == 400:
            logging.error("Bad Request: %s", response.text)
            return 8, status_code
        elif status_code == 401:
            logging.error("Unauthorized: %s", response.text)
            return 9, status_code
        elif status_code == 402:
            logging.error("Payment Required: %s", response.text)
            return 10, status_code
        elif status_code == 403:
            logging.error("Forbidden: %s", response.text)
            return 11, status_code
        elif status_code == 404:
            logging.error("Not Found: %s", response.text)
            return 12, status_code
        elif status_code == 500:
            logging.error("Internal Server Error: %s", response.text)
            return 13, status_code
        elif status_code == 502:
            logging.error("Bad Gateway: %s", response.text)
            return 14, status_code
        elif status_code == 503:
            logging.error("Service Unavailable: %s", response.text)
            return 15, status_code
        else:
            logging.error("Server returned status code %s", status_code)
            return 7, status_code

        return 0, status_code


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Command line argument parsing
    parser = argparse.ArgumentParser(description='Server Checker Tool')
    parser.add_argument('url', metavar='url', type=str, help='Server URL to check')
    args = parser.parse_args()

    # Perform server check
    checker = ServerChecker(args.url)
    exit_code, status_code = checker.check_status()

    # Log result
    if status_code is not None:
        logging.info("Server returned status code %s", status_code)
    if exit_code == 0:
        logging.info("Server check succeeded")
    else:
        logging.error("Server check failed with exit code %s", exit_code)