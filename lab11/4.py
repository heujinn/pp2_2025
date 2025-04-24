import psycopg2 as pgsql

def insertManyUsers():
    try:
        connection = pgsql.connect(
            database="postgres",
            user='postgres',
            password='5262',
            host='localhost',
        )
        con = connection.cursor()

        con.execute(r"""
            CREATE OR REPLACE FUNCTION many_users(names TEXT[], surnames TEXT[], phones TEXT[]) RETURNS TEXT[] AS $$
            DECLARE
                incorrect_data TEXT[];
                i INT := 1;
            BEGIN
                WHILE i <= array_length(names, 1) LOOP
                    IF length(phones[i]) <> 4 OR NOT phones[i] ~ '^\d+$' THEN
                        incorrect_data := array_append(incorrect_data, names[i] || ' - ' || phones[i]);
                    ELSE
                        INSERT INTO phones (name, surname, number) VALUES (names[i], surnames[i], phones[i]);
                    END IF;
                    i := i + 1;
                END LOOP;
                RETURN incorrect_data;
            END;
            $$ LANGUAGE plpgsql;
        """)

        connection.commit()
        print("Mission accomplished")
    except pgsql.Error as e:
        print("Error", e)
    finally:
        if connection:
            con.close()
            connection.close()
def many_users(names, surnames, phones):
    try:
        connection = pgsql.connect(
            database="postgres",
            user='postgres',
            password='5262',
            host='localhost',
        )
        con = connection.cursor()

        con.callproc('many_users', (names, surnames, phones))
        incorrect_data = con.fetchone()

        if incorrect_data:
            print("Incorrect:")
            for data in incorrect_data:
                print(data)
        else:
            print("Mission accomplished")

        connection.commit()

    except pgsql.Error as e:
        print("Error", e)
    finally:
        if connection:
            con.close()
            connection.close()

insertManyUsers()
names = ['Tair', 'Maksim']
surnames = ['Ospanov', 'Agafonov']
phones = ['9090','8903']
many_users(names, surnames, phones)