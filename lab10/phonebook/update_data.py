#change user first name or phone

import psycopg2

conn = psycopg2.connect(
	database="phonebook",
	user='postgres',
	password='2305',
	host='localhost',
)
cursor = conn.cursor()
conn.autocommit = True

#looking with the first and last name
oldName = str(input("Name you want to change: "))
oldSurname = str(input("Surname you want to change: "))
oldNumber = int(input("Number you want to change: "))
sql = f"select * from phones where name =\'{oldName}\' and surname = \'{oldSurname}\' and number = \'{oldNumber}\' "
cursor.execute(sql)
info = cursor.fetchall()

if len(info) > 0:
    newName = str(input("New name: "))
    newSurname = str(input("New surname: "))
    newNumber = int(input("New number: "))
    sqlUpdate = f"Update phones set number =\'{newNumber}\', name =\'{newName}\', surname =\'{newSurname}\' where name =\'{oldName}\' and surname = \'{oldSurname}\'; " 
    cursor.execute(sqlUpdate)
    print("Mission accomplished");
else:
    print("There is no that person")


conn.commit()
conn.close()