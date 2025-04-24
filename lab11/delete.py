import psycopg2 as pgsql

def deleteByPattern(pattern):
    try:
        connection = pgsql.connect(
            database="postgres",
            user='postgres',
            password='5262',
            host='localhost',
        )
        con = connection.cursor()

        query = """
            DELETE FROM phones
            WHERE name = %s 
            OR surname = %s 
            OR number = %s;
        """
        con.execute(query, (pattern, pattern, pattern))
        
        deleted_rows = con.rowcount
        print(f"Mission accomplished")
        connection.commit()

    except pgsql.Error as e:
        print("Error", e)
    finally:
        if connection:
            con.close()
            connection.close()

object = input('Write the value of row you want to delete: ')
deleteByPattern(object)