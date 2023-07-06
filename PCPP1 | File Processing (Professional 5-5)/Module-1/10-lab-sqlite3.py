"""Pre-requisites

Lab 1.2.1.2 - sqlite - Lab 1
Objectives

    improving the student's skills in interacting with the SQLite database;
    using known SQL statements.

Scenario

The application is almost ready. Let's add the missing functionalities to it:

    Create a method called change_priority, responsible for updating task priority. The method should get the id of the task from the user and its new priority (greater than or equal to 1).
    Create a method called delete_task, responsible for deleting single tasks. The method should get the task id from the user.
    Implement a simple menu consisting of the following options:

    1. Show Tasks
    2. Add Task
    3. Change Priority
    4. Delete Task
    5. Exit

where:

    Show Tasks (calls the show_tasks method)
    Add Task (calls the add_task method)
    Change Priority (calls the change_priority method)
    Delete Task (calls the delete_task method)
    Exit (interrupts program execution)

The program should obtain one of these options from the user, and then call the appropriate method of the TODO object. Choosing option 5 must terminate the program. A menu should be displayed in an infinite loop so that the user can choose an option multiple times."""
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

    def delete_task(self, id_task):
        try:
            self.cursor.execute('DELETE FROM tasks WHERE id = ?', (id_task,))
            self.conn.commit()
            print(f"Task ID{id_task} was successfully deleted")
        except:
            print("It could not be deleted, probably the id is wrong")
    def change_priority(self, priority, id_task):
        try:
            self.cursor.execute('UPDATE tasks SET priority = ? WHERE id = ?', (priority, id_task))
            self.conn.commit()
            print(f"The new value of priority is: {priority} of the Task {id_task}")
        except:
            print("The updated was not successfully")
    def menu(self):
        while True:
            print("TODO App Menu:")
            print("1. Show Tasks")
            print("2. Add Task")
            print("3. Change Priority")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                # name = input("Enter task name: ")
                self.show_tasks()
                # if task:
                #     print(task)
                # else:
                #     print("Task not found.")
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                try:
                    id_task = int(input("Enter task ID: "))
                    priority = int(input("Enter the new priority: "))
                    self.change_priority(priority=priority, id_task=id_task)
                except:
                    print("The input has to be an integer.")
            elif choice == '4':
                try:
                    id_task = int(input("Enter task ID: "))
                    self.delete_task(id_task=id_task)
                except:
                    print("The input has to be an integer.")
            elif choice == '5':
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