"""
Application refactoring

Refactoring is a very important process during software development. The main purpose of refactoring is to improve the quality of the code. Every programmer in their career will have to refactor either their own or someone else’s code sooner or later.

A very common mistake made by young adepts of the art of programming is to repeat the same pieces of code in different places in the application. In this case, refactoring consists of creating a function containing repetitive fragments. As a result, the code’s volume is reduced, and it becomes more readable.

You've probably noticed that adding new functionalities to our TODO application would be very difficult. This is a sign that our application requires refactoring. Below are suggestions for changes we can make:

    creating a class called TODO that will connect to the database in the constructor. If you want, you can implement a separate method called connect for this purpose;
    moving the code responsible for creating the taskstable to the method named create_tasks_table;
    creating a method called add_task that will get the task name and priority from the user instead of using hardcoded values.

Will we be able to easily implement, for example, the data display functionality after these changes? Find out about this later in the course.
"""
import sqlite3


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')

    def add_task(self):
        name = input('Enter task name: ')
        priority = int(input('Enter priority: '))

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()


app = Todo()
app.add_task()
