import products
import orders
import couriers
import utilities


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
        'Update order details',
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

def menu(statuses, courier_manager, product_manager, order_manager):
    while True:
        utilities.clear_screen()
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
                    orders.view_orders(order_manager)
                elif choice == 2:
                    orders.add_order(courier_manager, product_manager, order_manager)
                elif choice == 3:
                    orders.order_status(order_manager, statuses)
                elif choice == 4:
                    orders.update_order(order_manager, product_manager, courier_manager)
                elif choice == 5:
                    orders.delete_order(order_manager)
                elif choice == 6:
                    orders.sort_order_by_status(order_manager, statuses)
                elif choice == 7:
                    orders.sort_order_by_courier(order_manager, courier_manager)
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
