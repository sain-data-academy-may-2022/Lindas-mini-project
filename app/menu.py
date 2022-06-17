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
        banner()
        choice = main_menu()
        if choice == 'Exit':
            break

        elif choice == 'Products':
            utilities.clear_screen()
            while True:
                choice = product_menu()
                if choice == 'Go back':
                    break
                elif choice == 'View products':
                    list = product_manager.get_all()
                    utilities.print_list(list)
                elif choice == 'Add new product':
                    products.add_item(product_manager)
                elif choice == 'Update product':
                    products.update_item(product_manager)
                elif choice == 'Delete product':
                    products.delete_product(product_manager)

        elif choice == 'Orders':
            utilities.clear_screen()
            while True:
                choice = order_menu()
                if choice == 'Go back':
                    break
                elif choice == 'Show orders':
                    orders.view_orders(order_manager)
                elif choice == 'Add order':
                    orders.add_order(courier_manager, product_manager, order_manager)
                elif choice == 'Update order status':
                    orders.order_status(order_manager, statuses)
                elif choice == 'Update order details':
                    orders.update_order(order_manager, product_manager, courier_manager)
                elif choice == 'Delete order':
                    orders.delete_order(order_manager)
                elif choice == 'Show orders by status':
                    orders.sort_order_by_status(order_manager, statuses)
                elif choice == 'Show orders by courier':
                    orders.sort_order_by_courier(order_manager, courier_manager)

        elif choice == 'Couriers':
            utilities.clear_screen()
            while True:
                choice = courier_menu()
                if choice == 'Go back':
                    break
                elif choice == 'List of couriers':
                    list = courier_manager.get_all()
                    utilities.print_list(list)
                elif choice == 'Add courier':
                    couriers.add_courier(courier_manager)
                elif choice == 'Update courier':
                    couriers.update_courier(courier_manager)
                elif choice == 'Delete courier':
                    couriers.delete_courier(courier_manager)

def banner():
    print('''
   ___      _   _            _      _____ _     _      _                  
  / _ \___ | |_(_) ___  _ __( )__  /__   \ |__ (_)_ __| |_ ___  ___ _ __  
 / /_)/ _ \| __| |/ _ \| '_ \/ __|   / /\/ '_ \| | '__| __/ _ \/ _ \ '_ \ 
/ ___/ (_) | |_| | (_) | | | \__ \  / /  | | | | | |  | ||  __/  __/ | | |
\/    \___/ \__|_|\___/|_| |_|___/  \/   |_| |_|_|_|   \__\___|\___|_| |_|
                                                                          
    ''')