import requests

try:
    reply = requests.get('http://localhost:3000')
    print(reply.status_code)

    print(reply.headers)
    print(reply.headers['Content-Type'])

    print(reply.text)

    print(requests.codes.__dict__)

except requests.exceptions.Timeout:
    print('Sorry, Mr. Impatient, you didn\'t get your data')
except requests.exceptions.ConnectionError:
    print('Nobody\'s home, sorry!')
except requests.exceptions.InvalidURL:
    print('Recipient unknown!')
else:
    print('Here is your data, my Master!')


