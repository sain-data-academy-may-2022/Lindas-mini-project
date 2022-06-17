import pymysql


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
                SELECT o.*, c.name, c.address, c.phone, b.name AS courier, p.name AS product_name
                FROM `order` o
                JOIN customer c ON o.customer_id = c.id
                JOIN courier b ON o.courier_id = b.id
                JOIN order_product op ON op.order_id = o.id
                JOIN product p ON p.id = op.product_id
                ORDER BY o.id ASC
            ''')

            orders = {}
            order_products = {}

            for order in cursor.fetchall():
                order_id = order['id']
                product_name = order['product_name']

                if order_id in orders:
                    order_products[order_id].append(product_name)
                else:
                    orders[order_id] = order
                    order_products[order_id] = [product_name]

            for (order_id, order) in orders.items():
                del order['product_name']
                order['products'] = order_products[order_id]

            return list(orders.values())


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


    def update_products(self, order_id, product_ids):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "DELETE from order_product WHERE order_id = %s",
                (order_id)
            )
            for product_id in product_ids:
                cursor.execute(
                    "INSERT INTO order_product (order_id, product_id) VALUES (%s, %s)",
                    (order_id, product_id)
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
                ORDER BY o.id ASC
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
                ORDER BY o.id ASC
                ''',
                (courier_id))
            return cursor.fetchall()