#Implement deleting data from tables by username of phone
import psycopg2

conn = psycopg2.connect(
	database="phonebook",
	user='postgres',
	password='2305',
	host='localhost',
	
)
con = conn.cursor()
conn.autocommit = True

#looking with the first and last name
oldName = str(input("Name: "))
oldSurname = str(input("Surname: "))
sql = f"select * from phones where name =\'{oldName}\' and surname = \'{oldSurname}\' "
con.execute(sql)
info = con.fetchall()

if len(info) > 0:
    sqlUpdate = f"Delete from phones where  name =\'{oldName}\' and surname = \'{oldSurname}\'; " 
    con.execute(sqlUpdate)
    print("Mission accomplished");
else:
    print("There is no that person")

conn.commit()
conn.close()