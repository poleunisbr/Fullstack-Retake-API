import mysql.connector
from mysql.connector import Error
from config import settings


def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database=settings.DB_NAME
        )
        return connection
    except Error as error:
        print("Error connecting to database:", error)
        raise error


def execute_sql_query(sql_query, query_parameters=None):
    connection = None
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)  # Using dictionary cursor
        cursor.execute(sql_query, query_parameters)

        if sql_query.strip().upper().startswith("SELECT"):
            result = cursor.fetchall()  # Fetching results for SELECT queries
        else:
            connection.commit()  # Committing changes for INSERT/UPDATE/DELETE
            result = True

        cursor.close()
        return result

    except Error as exception:
        print("Error executing SQL query:", exception)
        raise exception  # Re-raising the exception for the caller to handle

    finally:
        if connection and connection.is_connected():
            connection.close()
