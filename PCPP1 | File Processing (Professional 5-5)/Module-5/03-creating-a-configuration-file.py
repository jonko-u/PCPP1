"""
Creating a configuration file

Creating a configuration file is as easy as parsing it. If you know how to work with dictionaries, it's a piece of cake. Let's look at a simple example of how to create a configuration file that you already know. Take a look at the code in the editor.

To create a configuration file, you should treat the ConfigParser object as a dictionary. Note that the section names are keys, while their options are listed in separate dictionaries. The above configuration is saved using the write method, which requires an open file to be passed in text mode. For this purpose, the built-in open method is used.

A configuration loaded using the read method can also be modified. To change a single option, simply set the new value to the appropriate key, and then save the file using the write method:

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

config['redis']['db'] = '1'

with open('config.ini', 'w') as configfile:
    config.write(configfile)

"""
import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {'host': 'localhost'}
config['mariadb'] = {'name': 'hello',
                     'user': 'root',
                     'password': 'password'}
config['redis'] = {
    'port': 6379,
    'db': 0
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)