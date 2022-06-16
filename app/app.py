from dbfuncs import ProductManager, CourierManager, OrderManager, open_connection
import utilities
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

product_manager = ProductManager(connection)
courier_manager = CourierManager(connection)
order_manager = OrderManager(connection)

menu.menu(statuses, courier_manager, product_manager, order_manager)

# Close connection here

connection.close()