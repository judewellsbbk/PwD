import sqlite3
import pandas as pd

DB = 'employee_db'

cursor = db.cursor()

cursor.execute('''
        CREATE TABLE Employee(
        FirstName text NOT NULL,
        Surname text NOT NULL,
        Dept text NOTNULL
''')