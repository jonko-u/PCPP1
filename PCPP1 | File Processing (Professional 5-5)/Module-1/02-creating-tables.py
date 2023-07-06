"""

sqlite3 – creating tables

When connecting to the database using the connect method, a Connection object is created. It has a very useful method called cursor. The method creates a Cursor object that allows any SQL statements to be executed in the database. What does it look like in practice? Let's look at the code responsible for creating the table called tasks:

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')


Calling the execute method executes the CREATE TABLE statement in our database. The execute method takes any single SQL statement and optional parameters necessary to execute the query. The variant with optional parameters will be presented when we discuss inserting data in the database.

NOTE: Running the above program twice will throw an exception with the following message: sqlite3.OperationError: table tasks already exists. This is because the statement is trying to re-create a table with the same name. The solution to this problem is to modify the query as follows:

CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);

"""
import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')
