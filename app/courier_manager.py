import pymysql


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