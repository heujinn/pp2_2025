import psycopg2 as pgsql

def searchRecords(pattern):
    try:
        connection = pgsql.connect(
            database="postgres",
            user='postgres',
            password='5262',
            host='localhost',
        )
        con = connection.cursor()
        query = "SELECT * FROM phones WHERE name LIKE %s OR surname LIKE %s OR number LIKE %s"
        con.execute(query, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
        records = con.fetchall()
        return records

    except pgsql.Error as e:
        print("Error", e)
    finally:
        if connection:
            con.close()
            connection.close()

pattern = str(input("Search:"))
foundedResults = searchRecords(pattern)
print("Result:")
for record in foundedResults:
    print(record)