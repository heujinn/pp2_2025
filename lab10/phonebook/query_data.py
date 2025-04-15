#Querying data from the tables 
import psycopg2

conn = psycopg2.connect(
	database="phonebook",
	user='postgres',
	password='2305',
	host='localhost',
)
cursor = conn.cursor()
conn.autocommit = True

#select all
#sql = f"select * from phones";

#select filter 
#sql = f"select * from phones where name = \'Abylay\' ";

#select with sort filter decrease by first
#sql = f"select * from phones by order by name desc";

#select with sort filter increase by first
#sql = f"select * from phones by order by name asc";

cursor.execute(sql)
info = cursor.fetchall()
print(info)