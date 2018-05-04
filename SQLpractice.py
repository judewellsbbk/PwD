#
# Examples on how to use Sqlite3, I
# Table creation and data insertion
# the db.commit() are there for good db practice
# folder ./sqlite should exist already (in this version)
#
import sqlite3
import pandas as pd


def main():
	# Create a database in RAM
	db = sqlite3.connect(':memory:')

	# Second step:
	# Create (or open) a SQLite3 DB hosted on file 'DB'
	DB = 'nursery_db'
	db = sqlite3.connect(DB)

	# Get a cursor object
	cursor = db.cursor()
	cursor.execute('''
		CREATE TABLE employees (
    		ssn     integer     PRIMARY KEY,
    		phone        integer        NOT NULL,
    		in_country  varchar(2),  -- country name (2 characters)
    		population  integer
			);
		''')
	db.commit()

	cursor = db.cursor()
	cursor.execute('''
		INSERT INTO cities (city_id, name, in_country, population) VALUES 
			(1,'London','GB', 8674000),
			(2,'Grayshott','GB', 2413),
			(3,'New York City','US', 8406000),
			(4,'Las Vegas','US', 603000),
			(5, 'Paris', 'FR', 10354000),
			(6, 'Beaumont', 'FR', 11000),
			(7, 'Los Angeles', 'US', 3884000),
			(8, 'San Juan', 'PR', 389714),
			(9, 'Millbrook', 'US', 8601)
		''')
	db.commit()

	# Insert from variables
	cid, name, country, pop = 10, 'Glasgow', 'GB', 606300

	cursor.execute('''
		INSERT INTO cities (city_id, name, in_country, population) 
		VALUES (?,?,?,?)''', (cid, name, country, pop) )
	db.commit()

	# feeding from dictionary:
	cid, name, country, pop = 11, 'Philadelphia', 'US', 1550000

	cursor.execute('''INSERT INTO cities (city_id, name, in_country, population) 
                  VALUES(:city_id, :name, :in_country, :population)''',
                  {'city_id':cid, 'name':name, 'in_country':country, 'population':pop})
	db.commit()

	db.close()


#main()

DB = 'cinema_db'

# open a file called mydb with a SQLite3 DB
db = sqlite3.connect(DB)

# Get a cursor object
cursor = db.cursor()

# model execution
cursor.execute('''SELECT city_id, population FROM cities''')

#retrieve the first city
# in this query, the order is undetermined, see ex. below
one_city = cursor.fetchone()
print(one_city[1])

all_rows = cursor.fetchall()
for row in all_rows:
	print('| {0} : {1}|'.format(row[0], row[1]))
#db.close()

# Finish here: use ORDER BY to print the most popolous city

#print(pd.read_sql('select city_id, population FROM cities', db))

print(pd.read_sql('select * FROM cities ORDER BY population desc', db))

ALTER TABLE {}

DB = 'employee_db'
