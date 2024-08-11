import mysql.connector
from config import db_host, db_user, db_password, db_name

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
            )
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to database:", error)
        return error

def execute_sql_query(sql_query, query_parameters=None):
    connection = connect_to_database()
    result = None
    try:
        cursor = connection.cursor(dictionary=True)  # Set dictionary=True
        cursor.execute(sql_query, query_parameters)
        if sql_query.upper().startswith("SELECT"):
            # executed for GET requests
            result = cursor.fetchall()
        else:
            # executed for POST requests
            connection.commit()
            result = True
    except mysql.connector.Error as exception:
        print("Error executing SQL query:", exception)
        result = exception
    finally:
        if connection.is_connected():
            connection.close()
    return result