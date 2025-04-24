import psycopg2 as pgsql

def insertToUpdate():
    try:
        connection = pgsql.connect(
            database="postgres",
            user='postgres',
            password='5262',
            host='localhost',
        )
        con = connection.cursor()
        con.execute("""
            CREATE OR REPLACE FUNCTION insertToUpdateUser(name_param TEXT, surname_param TEXT, number_param TEXT) 
            RETURNS VOID AS 
            $$
            BEGIN
                IF EXISTS (SELECT 1 FROM phones WHERE name = name_param OR surname = surname_param) THEN
                    UPDATE phones SET number = number_param WHERE name = name_param OR surname = surname_param;
                ELSE
                    INSERT INTO phones (name, surname, number) VALUES (name_param, surname_param, number_param);
                END IF;
            END;
            $$
            LANGUAGE plpgsql;
        """)
        connection.commit()
    except pgsql.Error as e:
        print("Error", e)
    finally:
        if connection:
            con.close()
            connection.close()

def insertToUpdateUser(name, surname, number):
    try:
        connection = pgsql.connect(
            database="postgres",
            user='postgres',
            password='5262',
            host='localhost',
        )
        con = connection.cursor()
        con.callproc('insertToUpdateUser', (name, surname, number))
        connection.commit()

    except pgsql.Error as e:
        print("Error", e)
    finally:
        if connection:
            con.close()
            connection.close()

insertToUpdate()
insertToUpdateUser('Gaukhar', 'Ulasova', '2010')