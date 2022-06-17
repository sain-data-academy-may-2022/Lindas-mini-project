import pymysql


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