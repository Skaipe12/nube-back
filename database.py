import mysql.connector
from mysql.connector import Error

def connect():
    try:
        connection = mysql.connector.connect(
            user='nube_database_user',
            password='password',
            host='44.202.243.10',
            port='3306',
            database='movies'
        )
        if connection.is_connected():
            print(connection)
            return connection
    except Error as e:
        print(f"Error: {e}")

def get_connection():
    return connect()

def close_connection(connection):
    if connection.is_connected():
        connection.close()
