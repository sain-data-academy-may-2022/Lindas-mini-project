import products
import orders
import couriers
import utilities


my_products = ['Pepper up', 'Draught of Peace', 'Amorentia', 'Fatigue Infusion', 'Invisibility potion']
my_couriers = ['Gil', 'Ansis', 'Liene', 'Jasmina']
my_orders = [   
    {'name': 'Billy', 'address': '25 Baker street', 'phone': '111119992', 'status': 'PREPARING'},
    {'name': 'Lisa', 'address': '26 Plam street', 'phone': '676767676', 'status': 'PREPARING'},
    {'name': 'Richard', 'address': 'Down with surveillance!!!!!!', 'phone': '00000', 'status': 'PREPARING'},
]


def main_menu():   
    return utilities.get_choice([
        'Exit program',
        'View products',
        'View orders',
        'Couriers',
    ])
    

def product_menu():   
    return utilities.get_choice([
        'Return to main menu',
        'View products',
        'Add new product',
        'Update product',
        'Delete product',
    ])
 

def order_menu():
    return utilities.get_choice([
        'Return to main menu',
        'Show orders',
        'Add order',
        'Update order status',
        'Update items in the order',
        'Delete order',
    ])


def courier_menu():
    return utilities.get_choice([
        'Return to main menu',
        'List of couriers',
        'Add courier',
        'Update courier',
        'Delete courier',
    ])


while True:
    choice = main_menu()
    if choice == 0:
        break
    elif choice == 1:
        while True:
            choice = product_menu()
            if choice == 0:
                break
            elif choice == 1:
                utilities.print_list(my_products)
            elif choice == 2:
                products.add_item(my_products)
            elif choice == 3:
                products.update_item(my_products)
            elif choice == 4:
                products.remove_item(my_products)
    elif choice == 2:
        while True:
            choice = order_menu()
            if choice == 0:
                break
            elif choice == 1:
                utilities.print_list(my_orders)
            elif choice == 2:
                orders.add_order(my_orders)
            elif choice == 3:
                orders.order_status(my_orders)
            elif choice == 4:
                orders.update_order(my_orders)
            elif choice == 5:
                orders.remove_order(my_orders)
    elif choice == 3:
        while True:
            choice = courier_menu()
            if choice ==0:
                break
            elif choice == 1:
                utilities.print_list(my_couriers)
            elif choice == 2:
                couriers.add_courier(my_couriers)
            elif choice == 3:
                couriers.update_courier(my_couriers)
            elif choice == 4:
                couriers.remove_courier(my_couriers)
                