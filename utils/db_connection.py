import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",     
            database="placement"
        )
        return connection
    except mysql.connector.Error as err:
        print("Error:", err)
        return None
