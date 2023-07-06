"""

sqlite3 – updating data

Each of the tasks created has its own priority, but what if we decide that one of them should be done earlier than the others. How can we increase its priority? We have to use the SQL statement called UPDATE.

The UPDATE statement is used to modify existing records in the database. Its syntax is as follows:

UPDATE table_name
SET column1 = value1, column2 = value2, column3 = value3, …, columnN = valueN
WHERE condition;

If we'd like to set the priority to 20 for a task with idequal to 1, we can use the following query:

UPDATE tasks SET priority = 20 WHERE id = 1;

NOTE: If you forget about the WHERE clause, all data in the table will be updated.

As before, we execute all SQL statements using the execute method. Look at the code in the editor.

"""
import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (20, 1))
conn.commit()
c.close()