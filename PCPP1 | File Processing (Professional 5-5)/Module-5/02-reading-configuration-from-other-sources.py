"""

Reading configuration from other sources

The configparser module enables configurations from various sources to be read. One of them is a dictionary that we can load using the read_dict. Look at the code in the editor.

Result:

Sections: ['mariadb', 'redis']

mariadb section:
Host: localhost
Database: hello
Username: root
Password: password

redis section:
Host: localhost
Port: 6379
Database number: 0

The read_dict method accepts any dictionary whose keys are section names, while the values include dictionaries containing keys and values. All values read from the dictionary are converted to strings.

NOTE: The configparser module also has read_file and read_string methods that allow you to read the configuration from an open file or string. You can find more information about these methods in the documentation.

"""
import configparser

config = configparser.ConfigParser()

dict = {
    'DEFAULT': {
        'host': 'localhost'
    },
    'mariadb': {
        'name': 'hello',
        'user': 'root',
        'password': 'password'
    },
    'redis': {
        'port': 6379,
        'db': 0
    }
}

config.read_dict(dict)

print('Sections:', config.sections(),'\n')

print('mariadb section:')
print('Host:', config['mariadb']['host'])
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', int(config['redis']['port']))
print('Database number:', int(config['redis']['db']))
