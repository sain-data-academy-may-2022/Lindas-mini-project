from dbfuncs import ProductManager
from dbfuncs import CourierManager
import products
import orders
import couriers
import utilities

my_orders = utilities.import_json('orders.json')

product_manager = ProductManager()
courier_manager = CourierManager()

statuses = [
    'PENDING',
    'PICKING',
    'PREPARING',
    'DISPATCHED',
    'DELIVERED',
]

def main_menu():  
    return utilities.get_choice([
        'Exit',
        'Products',
        'Orders',
        'Couriers',
    ])
    

def product_menu():   
    return utilities.get_choice([
        'Go back',
        'View products',
        'Add new product',
        'Update product',
        'Delete product',
    ])
 

def order_menu():
    return utilities.get_choice([
        'Go back',
        'Show orders',
        'Add order',
        'Update order status',
        'Update items in the order',
        'Delete order',
        'Show orders by status',
        'Show orders by courier',
    ])


def courier_menu():
    return utilities.get_choice([
        'Go back',
        'List of couriers',
        'Add courier',
        'Update courier',
        'Delete courier',
    ])

utilities.clear_screen()
while True:
    choice = main_menu()
    if choice == 0:
        break
    elif choice == 1:
        utilities.clear_screen()
        while True:
            choice = product_menu()
            if choice == 0:
                break
            elif choice == 1:
                list = product_manager.get_all()
                utilities.print_list(list)
            elif choice == 2:
                products.add_item(product_manager)
            elif choice == 3:
                products.update_item(product_manager)
            elif choice == 4:
                products.delete_product(product_manager)
    elif choice == 2:
        utilities.clear_screen()
        while True:
            choice = order_menu()
            if choice == 0:
                break
            elif choice == 1:
                utilities.print_list(my_orders)
            elif choice == 2:
                orders.add_order(my_orders, courier_manager, product_manager)
            elif choice == 3:
                orders.order_status(my_orders, statuses)
            elif choice == 4:
                orders.update_order(my_orders, product_manager, courier_manager)
            elif choice == 5:
                orders.delete_order(my_orders)
            elif choice == 6:
                orders.sort_order_by_status(my_orders, statuses)
            elif choice == 7:
                orders.sort_order_by_courier(my_orders, courier_manager)
    elif choice == 3:
        utilities.clear_screen()
        while True:
            choice = courier_menu()
            if choice ==0:
                break
            elif choice == 1:
                list = courier_manager.get_all()
                utilities.print_list(list)
            elif choice == 2:
                couriers.add_courier(courier_manager)
            elif choice == 3:
                couriers.update_courier(courier_manager)
            elif choice == 4:
                couriers.delete_courier(courier_manager)
                