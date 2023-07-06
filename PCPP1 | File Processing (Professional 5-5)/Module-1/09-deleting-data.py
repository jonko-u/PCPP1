"""
sqlite3 – deleting data

After completing a task, we would like to remove it from our database. To do this, we must use the SQL statement called DELETE:

DELETE FROM table_name WHERE condition;

Let's look at what removing the task with id = 1might look like:

DELETE FROM tasks WHERE id = 1;

NOTE: If you forget about the WHERE clause, all data in the table will be deleted.

Look at the code in the editor to see how to delete a record using the sqlite3 module.
"""
import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('DELETE FROM tasks WHERE id = ?', (1,))
conn.commit()
c.close()