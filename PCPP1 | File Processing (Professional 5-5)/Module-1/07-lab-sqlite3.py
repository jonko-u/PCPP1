"""
Level of difficulty

Easy
Estimated time

15 minutes
Objectives

    improving the student's skills in interacting with the SQLite database;
    using known methods of the Cursor object.

Scenario

Our TODO application requires you to add a little security and display the data saved in the database. Your task is to implement the following functionalities:

    Create a find_task method, which takes the task name as its argument. The method should return the record found or None otherwise.
    Block the ability to enter an empty task (the name cannot be an empty string).
    Block the ability to enter a task priority less than 1.
    Use the find_task method to block the ability to enter a task with the same name.
    Create a method called show_tasks, responsible for displaying all tasks saved in the database.

Test data:
Example input:

Enter task name: My first task
Enter priority: 1
Example output:

(1, 'My first task', 1)
Example input:

Enter task name: My second task
Enter priority: 2
Example output:

(1, 'My first task', 1)
(2, 'My second task', 2)
Example input:

Enter task name: My first task
Enter priority: 1
Example output:

(1, 'My first task', 1)
(2, 'My second task', 2)

"""
import sqlite3
from package.package.frame import Frame


class Todo:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_task_table()

    def add_task(self):
        name = input("Enter task name: ")
        if not name:
            print("Task name cannot be empty.")
            return
        priority = int(input("Enter priority: "))
        if priority < 1:
            print("Priority must be greater than or equal to 1.")
            return
        if self.find_task(name):
            print("Task with the same name already exists.")
            return
        self.cursor.execute("INSERT INTO tasks (name, priority) VALUES (?, ?)", (name, priority))
        self.conn.commit()
        print("Task added successfully.")

    def find_task(self, name):
        self.cursor.execute("SELECT * FROM tasks WHERE name=?", (name,))
        return self.cursor.fetchone()
    def create_task_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')

    def show_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        tasks = self.cursor.fetchall()
        for task in tasks:
            print(task)

    def menu(self):
        while True:
            print("TODO App Menu:")
            print("1. Find a task")
            print("2. Add a task")
            print("3. Show tasks")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")
            if choice == '1':
                name = input("Enter task name: ")
                task = self.find_task(name)
                if task:
                    print(task)
                else:
                    print("Task not found.")
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.show_tasks()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def __del__(self):
        self.conn.close()

if __name__ == '__main__':
    menu_frame = Frame("lab-sqlite3", width=30, border="+", padding="-")
    print(menu_frame.draw())
    todo = Todo('todo.db')
    todo.menu()