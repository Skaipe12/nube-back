import psycopg2

def connect():
        try:
            connection = psycopg2.connect(
                user='postgres',
                password='password',
                host='http://18.233.152.87',
                port='5432',
                database='movies'
            )
            return connection
        except psycopg2.DatabaseError as e:
            print(f"Error: {e}")

def get_connection():
    return connect()

def close_connection(connection):
    connection.close()