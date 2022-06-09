import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")


# Establish a database connection

def open_connection():
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    return connection


# Closes the connection to the DB, make sure you ALWAYS do this

def close_connection(connection):
    connection.close()


# Product manager that does all DB inputs

class ProductManager:
    def create(self, name, price):
        connection = open_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO product (name, price) VALUES (%s, %s)"
        val = (name, price)
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        close_connection(connection)

    def get_all(self):
        connection = open_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM product')
        rows = cursor.fetchall()
        cursor.close()
        close_connection(connection)
        return rows

    def update(self, id, name, price):
        connection = open_connection()
        cursor = connection.cursor()
        sql = "UPDATE product SET name = %s, price = %s WHERE id = %s"
        val = (name, price, id)
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        close_connection(connection)

    def delete(self, id):
        connection = open_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM product WHERE id = %s"
        val = (id)
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        close_connection(connection)


# Courier manager that does all DB inputs

class CourierManager:
    def create(self, name, phone):
        connection = open_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO courier (name, phone) VALUES (%s, %s)"
        val = (name, phone)
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        close_connection(connection)

    def get_all(self):
        connection = open_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM courier')
        rows = cursor.fetchall()
        cursor.close()
        close_connection(connection)
        return rows

    def update(self, id, name, phone):
        connection = open_connection()
        cursor = connection.cursor()
        sql = "UPDATE courier SET name = %s, phone = %s WHERE id = %s"
        val = (name, phone, id)
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        close_connection(connection)
    
    def delete(self, id):
        connection = open_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM courier WHERE id = %s"
        val = (id)
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        close_connection(connection)














# # Closes the cursor so will be unusable from this point 
# cursor.close()

# connection.commit()
