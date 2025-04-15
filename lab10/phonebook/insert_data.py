import csv 
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='phonebook',
    user='postgres',
    password='2305')

con = conn.cursor()
arr=[]

#First way
with open('list.csv') as f:
    f_read = csv.reader(f, delimiter='-')
    for row in f_read:
        row[0] = int(row[0].strip('-'))
        arr.append(row)

insertQuery = """ INSERT INTO  phones VALUES (%s,%s,%s,%s) RETURNING *;"""

for i in arr:
    con.execute(insertQuery, i)

conn.commit()
print("Mission accomplished")
conn.close()

#Second way
name = str(input("Name: "))
surname = str(input("Surname: "))
number = int(input("Number: "))

insertQuery = """ INSERT INTO  phones(name, surname, number) VALUES (%s,%s,%s)"""
recordToInsert = (name, surname, number)
con.execute(insertQuery, recordToInsert)

conn.commit()
print("Mission accomplished");
conn.close()