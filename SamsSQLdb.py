import sqlite3

conn = sqlite3.connect('gallery.sql')


# employee table
cursor = db.cursor()
cursor.execute(
    CREATE TABLE Employee (
        FirstName    text NOT NULL,
       Surname        text        NOT NULL,
       Dept  text NOT NULL,
       Office  varchar NOT NULL,
       Salary integer NOT NULL,
       City text NOT NULL
        );
    )
db.commit()

cursor.execute(
    INSERT INTO Employee (FirstName, Surname, Dept, Office, Salary, City) VALUES
       ('Mary', 'Brown', 'Administration', '10', 45, 'London'),
        ('Charles', 'White', 'Production', '20', 36, 'Toulouse'),
       ('Gus', 'Green', 'Administration', '20', 40, 'Oxford'),
       ('Jackson', 'Neri', 'Distribution', '16', 45, 'Dover'),
       ('Charles', 'Brown', 'Planning', '20', 80, 'London'),
       ('Laurence', 'Chen', 'Planning', '20', 73, 'Worthing'),
       ('Pauline', 'Bradshaw', 'Administration', '75', 40, 'Brighton'),
       ('Alice', 'Jackson', 'Production', '20', 46, 'Toulouse')

    )
db.commit()

# department table
cursor.execute(
    CREATE TABLE Department (
        DeptName    text     NOT NULL,
       Address        text        NOT NULL,
       City  text NOT NULL
        );
    )
db.commit()

cursor.execute(
    INSERT INTO Department (DeptName, Address, City) VALUES
       ('Administration', 'Bond Street', 'London'),
        ('Production', 'Rue Victor Hugo', 'Toulouse'),
       ('Distribution', 'Pond Road', 'Brighton'),
       ('Planning', 'Bond Street', 'London'),
       ('Research', 'Sunset Street', 'San Jose')

    )
db.commit()

# Check
import pandas as pd

employee = pd.read_sql('select * from employee', db)
print(employee)

dep = pd.read_sql('select * from department', db)
print(dep)