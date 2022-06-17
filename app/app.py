from dbfuncs import open_connection
from product_manager import ProductManager
from courier_manager import CourierManager
from order_manager import OrderManager
import menu


statuses = [
    'PENDING',
    'PICKING',
    'PREPARING',
    'DISPATCHED',
    'DELIVERED',
]




# Open connection here

connection = open_connection()

product_man = ProductManager(connection)
courier_man = CourierManager(connection)
order_man = OrderManager(connection)

menu.menu(statuses, courier_man, product_man, order_man)

# Close connection here

connection.close()