"""

sqlite3 – creating a database

As we already said, the SQLite database is a single file, which is saved on your computer. Each file, regardless of the operating system used, has its location (a path to a specific disk space). When you create a database, you can create it in your current working directory, or in any other location. To create a database, use the connect method provided by the sqlite3 module:

import sqlite3

conn = sqlite3.connect('hello.db')

The connect method returns the database representation as a Connection object. In the example above, the method takes only the database name as the argument. This means that the database will be created in the same directory as the script that wants to access it. If you'd like to create a database in the sqlite3 directory on your C disk you can do this as follows:

import sqlite3

conn = sqlite3.connect('C:\sqlite\hello.db')

It's also possible to use a special name, :memory:, which creates a database in RAM:

import sqlite3

conn = sqlite3.connect(':memory:')

Remember that the connect method creates a database only if it cannot find a database in the given location. If a database exists, SQLite connects to it.

Python & database connection


A few words about SQL

You’ve already learned how to create a database in Python using the sqlite3 module. It's now time to discuss how we can create its structure. For this purpose, we’ll need some knowledge of SQL.

SQL is a Structured Query Language for creating, modifying, and managing relational databases. It’s used by the most popular database management systems such as MySQL, PostgreSQL, and our favorite SQLite. The SQL language was developed in the 70s by IBM. Over the years, SQL has been modified by many companies that have implemented it in their products. Therefore, it became necessary to introduce a standard that would standardize its syntax.

Since the first production deployments, the following standards have been created: SQL-86, SQL-89, SQL-92, SQL:1999, SQL:2003, SQL:2006, SQL:2008, SQL:2011, SQL:2016, SQL:2019. Detailed information on each of the standards can be found in the Internet resources. It’s worth mentioning that SQLite generally implements the SQL-92 standard, with some exceptions that you can read about here.

SQL syntax and its standards are extensive topics. Fortunately, there are many free materials available on the Internet to help you acquire some basic knowledge. We encourage you to familiarize yourself with them.

If you've never dealt with SQL before, don't worry. All examples including SQL will be explained in detail.
"""
import sqlite3

conn = sqlite3.connect('hello.db')
