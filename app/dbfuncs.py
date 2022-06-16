import pymysql
import os
from dotenv import load_dotenv
from pyrsistent import s

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


# Product manager that does all DB inputs

class ProductManager:
    def __init__(self, connection):
        self.connection = connection


    def create(self, name, price):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO product (name, price) VALUES (%s, %s)",
                (name, price)
            )
            self.connection.commit()


    def get_all(self):
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute('SELECT * FROM product')
            return cursor.fetchall()


    def update(self, id, name, price):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE product SET name = %s, price = %s WHERE id = %s",
                (name, price, id)
            )
            self.connection.commit()


    def delete(self, id):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM product WHERE id = %s",
                (id)
            )
            self.connection.commit()


# Courier manager that does all DB inputs

class CourierManager:
    def __init__(self, connection):
        self.connection = connection


    def create(self, name, phone):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO courier (name, phone) VALUES (%s, %s)",
                (name, phone)
            )
            self.connection.commit()
      

    def get_all(self):
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute('SELECT * FROM courier')
            return cursor.fetchall()
        

    def update(self, id, name, phone):
       with self.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE courier SET name = %s, phone = %s WHERE id = %s", 
                (name, phone, id)
            )
            self.connection.commit()
            

    def delete(self, id):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM courier WHERE id = %s", 
                (id)
            )
            self.connection.commit()


# Order manager that does all DB inputs

class OrderManager:
    def __init__(self, connection):
        self.connection = connection


    def create(self, name, address, phone, status, product_ids, courier_id):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO customer (name, address, phone) VALUES (%s, %s, %s)", 
                (name, address, phone)
            )
            customer_id = cursor.lastrowid

            cursor.execute(
                "INSERT INTO `order` (customer_id, courier_id, status) VALUES (%s, %s, %s)",
                (customer_id, courier_id, status)
            )
            order_id = cursor.lastrowid

            for product_id in product_ids:
                cursor.execute(
                    "INSERT INTO order_product (product_id, order_id) VALUES (%s, %s)",
                    (product_id, order_id)
                )
                
            self.connection.commit()
          
    
    def get_all(self):
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute('''
                SELECT o.*, c.name, c.address, c.phone, b.name AS courier
                FROM `order` o
                JOIN customer c ON o.customer_id = c.id
                JOIN courier b ON o.courier_id = b.id''')
            return cursor.fetchall()


    def update_courier(self, id, courier_id):
       with self.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE `order` SET courier_id = %s WHERE id = %s", 
                (courier_id, id)
            )
            self.connection.commit()


    def update_customer_name(self, customer_id, name):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE customer SET name = %s WHERE id = %s",
                (name, customer_id)
            )
            self.connection.commit()


    def update_customer_address(self, customer_id, address):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE customer SET address = %s WHERE id = %s",
                (address, customer_id)
            )         
            self.connection.commit()


    def update_customer_phone(self, customer_id, phone):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE customer SET phone = %s WHERE id = %s",
                (phone, customer_id)
            )
            self.connection.commit()
     

    def update_order_status(self, order_id, status):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE `order` SET status = %s WHERE id = %s",
                (status, order_id)
            )
            self.connection.commit()


    def delete_order(self, order_id, customer_id):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "DELETE from order_product WHERE order_id = %s",
                (order_id)
            )
            cursor.execute(
                "DELETE from `order` WHERE id = %s",
                (order_id)
            )
            cursor.execute(
                "DELETE from customer WHERE id = %s",
                (customer_id)
            )
            self.connection.commit()

    def view_orders_by_status(self, status):
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute('''
                SELECT o.*, c.name, c.address, c.phone, b.name AS courier
                FROM `order` o
                JOIN customer c ON o.customer_id = c.id
                JOIN courier b ON o.courier_id = b.id
                WHERE o.status = %s
                ''',
                (status))
            return cursor.fetchall()


    def view_orders_by_courier(self, courier_id):
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute('''
                SELECT o.*, c.name, c.address, c.phone, b.name AS courier
                FROM `order` o
                JOIN customer c ON o.customer_id = c.id
                JOIN courier b ON o.courier_id = b.id
                WHERE o.courier_id = %s
                ''',
                (courier_id))
            return cursor.fetchall()