#
# Examples on how to use Sqlite3, I
# Table creation and data insertion
# the db.commit() are there for good db practice
# folder ./sqlite should exist already (in this version)
#
import sqlite3
import pandas as pd

conn = sqlite3.connect("Training.db") #This will create the file if it does not yet exist

c = conn.cursor()

#c.execute("DROP TABLE iceCubeMelting")

c.execute("CREATE TABLE IF NOT EXISTS iceCubeMelting(time INT PRIMARY KEY, temperature REAL, date TEXT)")
#conn.commit()

c.execute("SELECT time FROM iceCubeMelting")
result = c.fetchone() # Kind of equivalent to f.readline()
#print(result)
result = c.fetchmany(size = 5)
#print(result)
result = c.fetchall() #kind of equivalent to f.read() - note that it depends where the file marker is (if you have already reaa few rows you will not return these
#print(result)
"""
c.execute("CREATE TABLE tablename(column1Name datatype PRIMARY KEY," +
          "column2Name datatype, column3Name datatype)")

c.execute("DROP TABLE iceCubeMelting")
c.execute("INSERT INTO tablename VALUES (value1, value2, value3...)")
"""

#c.execute("INSERT INTO iceCubeMelting VALUES"+
#           "(1, 27.0, '28-08-2017')")

# for i in range(1,5):
#     c.execute("INSERT INTO iceCubeMelting (time, temperature, date)"+
#               " VALUES (?,?,?)", (i, 27 - 0.1*i, '28-08-2017'))
#
# for i in range(5, 8):
#     c.execute("INSERT INTO iceCubeMelting (time, temperature)"+
#               " VALUES (?,?)", (i, 27 - 0.1*i))
#
# for i in range(8, 10):
#     c.execute("INSERT INTO iceCubeMelting (temperature, time)"+
#           " VALUES (?,?)", (27 - 0.1*i, i))


# c.execute("SELECT time, temperature, date FROM iceCubeMelting")

#SELECT * FROM tablename LIMIT #NoRows OFFSET #offset
#c.execute("SELECT * FROM iceCubeMelting LIMIT 2 OFFSET 1 ")
#c.execute("SELECT * FROM iceCubeMelting ORDER BY temperature DESC")

c.execute("SELECT * FROM iceCubeMelting WHERE date = '28-08-2017'")
c.execute("SELECT * FROM iceCubeMelting WHERE date IS NOT NULL")
c.execute("SELECT * FROM iceCubeMelting WHERE time > 5 AND temperature > 26.2")
c.execute("SELECT * FROM iceCubeMelting WHERE time < 5 OR temperature > 26.2")
c.execute("UPDATE iceCubeMelting SET date = '30-08-2017', temperature = 26.5 WHERE time > 6")
c.execute("DELETE FROM iceCubeMelting Where time < 5")

data = c.fetchall()
for piece in data:
    print(piece)

conn.commit()
c.close()
conn.close()
