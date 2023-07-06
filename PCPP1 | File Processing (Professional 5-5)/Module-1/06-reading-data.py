"""

sqlite3 – reading data (part 1)

So far, we haven't displayed any information on the screen about the inserted tasks. It's time to change that. Let's see what’s in our database. We’ll first need the appropriate SQL statement, named SELECT.

The SELECT statement allows you to read data from one or more tables. Its syntax looks like this:

SELECT column FROM table_name;

or

SELECT column1, column2, column3, …, columnN FROM table_name;

or

SELECT * FROM table_name;

In the first variant, we decide to read the values saved in only one column. If we'd like to read only the names of the tasks saved in the tasks table, we could use the following query:

SELECT name FROM tasks;

The second variant allows you to read values from more columns. If we'd like to read the task names and their priorities, we could use the following query:

SELECT name, priority FROM tasks;

If we don’t have any specific requirements, we can read the values from all columns:

SELECT * FROM tasks;

The last variant will display the values saved in the id, name and priority columns.

sqlite3 – reading data (part 2)

It probably won’t surprise you to learn that reading data saved in the database is done with the well-known Cursor object. After calling the execute method with the appropriate SELECT statement, the Cursor object is treated as an iterator. Look at the code in the editor.

Result:

(1, 'My first task', 1)
(2, 'My second task', 5)
(3, 'My third task', 10)

The variable row in each iteration takes a row in the form of a tuple. Access to individual columns is done using an index, e.g., print (row [0]) will display the values saved in the id column.

sqlite3 – reading data (part 3)

If you don't want to treat the Cursor object as an iterator, you can use its method called fetchall. The fetchall method fetches all records (those not yet fetched from the query result). Look at the code in the editor.

Result:

(1, 'My first task', 1)
(2, 'My second task', 5)
(3, 'My third task', 10)

The fetchall method is less efficient than the iterator, because it reads all records into the memory and then returns a list of tuples. For small amounts of data, it doesn't matter, but if your table contains a huge number of records, this can cause memory issues.

NOTE: The fetchall method returns an empty list when no rows are available.

sqlite3 – reading data (part 3)

If you don't want to treat the Cursor object as an iterator, you can use its method called fetchall. The fetchall method fetches all records (those not yet fetched from the query result). Look at the code in the editor.

Result:

(1, 'My first task', 1)
(2, 'My second task', 5)
(3, 'My third task', 10)

The fetchall method is less efficient than the iterator, because it reads all records into the memory and then returns a list of tuples. For small amounts of data, it doesn't matter, but if your table contains a huge number of records, this can cause memory issues.

NOTE: The fetchall method returns an empty list when no rows are available.

sqlite3 – reading data (part 4)

In addition to the iterator and the fetchall method, the Cursor object provides a very useful method called fetchone to retrieve the next available record. Look at the code in the editor.

Result:

(1, 'My first task', 1)
(2, 'My second task', 5)

NOTE: The fetchone method returns None if there is no data to read.

"""
import sqlite3


# Part2
# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# for row in c.execute('SELECT * FROM tasks'):
#     print(row)
# conn.close()
# Part3 fetchall returns an empty list when no rows are available
# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('SELECT * FROM tasks')
# rows = c.fetchall()
# for row in rows:
#     print(row)
# conn.close()
# Part4 The fetchone method returns None if there is no data to read
conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('SELECT * FROM tasks')
row = c.fetchone()
print(row)
row = c.fetchone()
print(row)
row = c.fetchone()
print(row)
conn.close()