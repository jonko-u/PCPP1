"""
Parsing the configuration file

Parsing the configuration file is extremely simple. First, we need to create a ConfigParser object, which provides many useful methods for parsing data. One of them is the read method, responsible for reading and parsing the configuration file. In our example, we pass the config.ini filename to it, but it's also possible to pass a list containing several files.

If all goes well, the read method returns a list of filenames that have been successfully parsed. Let's look at the code in the editor to see how to parse the data stored in the config.ini file.

Result:

Sections: ['mariadb', 'redis']

mariadb section:
Host: localhost
Database: hello
Username: user
Password: password

redis section:
Host: localhost
Port: 6379
Database number: 0

In the example, we use the sections method to display the names of sections in the file. Note that the DEFAULT section doesn't appear in the list of returned sections. This is the default behavior of the sections method.

Access to the data contained in the configuration file is analogous to how we use dictionaries. To obtain any value, use the appropriate key sequence. It's important to note that the section names are case sensitive, while the keys aren't.

Despite the fact that the DEFAULT section is omitted as a result of the sections method, we still have access to its options. Both the mariadb and redis sections can read the host option.

Its also possible to access the values stored in the options by using the get method. The get method requires the section name and key to be passed. This is what it looks like in practice:

print('Host:', config.get('mariadb', 'host')) # print('Host:', config['mariadb']['host'])

"""
import configparser

config = configparser.ConfigParser()
print(config.read('config.ini'))

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