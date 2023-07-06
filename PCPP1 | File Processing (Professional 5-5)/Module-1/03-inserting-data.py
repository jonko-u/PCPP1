"""

sqlite3 – inserting data (part 1)

Congratulations. You’ve just created your first table in the database. It's time to fill it with data. Once again, a little knowledge of the SQL language will be invaluable, namely the INSERT INTO statement.

The INSERT INTO statement is used to insert records in a table. Its syntax is as follows:
INSERT INTO table_name (column1, column2, column3, ..., columnN)
VALUES (value1, value2, value3, ..., value4);

Using the above formula, we’re able to prepare a query that will allow us to save our first task in the database:
INSERT INTO tasks (id, name, priority) VALUES (1, 'My first task', 1);

or
INSERT INTO tasks (name, priority) VALUES ('My first task', 1);


You've probably noticed that in the second variant the id column is omitted. In this case, we inform the database management system of the desire to use auto-incrementation (a unique value is generated for us when a new record is inserted).

Of course, we can define the value of the id column ourselves, but it's more convenient not to worry about it.

The INSERT INTO statement also has a short form in which we can omit the column names:
INSERT INTO table_name VALUES (value1, value2, value3, ..., valueN);

sqlite3 – inserting data (part 2)

Let's look at how to use the INSERT INTO statement in our TODO project. Analyze the code in the editor.

The mysterious characters ? used in the INSERT INTO statement are query parameters that are replaced with the correct values during the execution of the statement. In the above example, the first character ? will be replaced with My first task, while the second will be replaced with l.

This is to avoid an SQL injection attack in which malicious SQL is appended to a query that could possibly destroy our database. You can find more information about SQL injection and possible safeguard measures on the Internet.

The execute method, as we mentioned before, has an optional argument in the form of an array of parameters. In our case, it takes a tuple, but it can be a simple array containing the same number of elements as the query parameters.

Our code isn't working properly yet, but don't worry. In a moment, you’ll learn a new method that will fix this problem.

"""
import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')
c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('My first task', 1))

"""
sqlite3 – inserting data (part 3)

We’re only one step away from inserting our first task in the database. All we're missing is to call the commit method provided by the Connection object. Look at the code in the editor.

The commit method confirms our changes (the current transaction). If you forget to call it, your changes won't be visible in the database.

In the example above, another method of the Connection object is used. The close method closes the database connection, e.g., after inserting all tasks.

NOTE: Restarting the program will create another task with the same name and priority, but with a different value that is auto-incremental.
"""
conn.commit()
conn.close()