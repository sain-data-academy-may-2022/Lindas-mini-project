import products
import orders
import utilities


my_products = ['Pepper up', 'Draught of Peace', 'Amorentia', 'Fatigue Infusion', 'Invisibility potion']
my_orders = [   
    {'name': 'Billy', 'address': '25 Baker street', 'phone': '111119992', 'status': 'PREPARING'},
    {'name': 'Lisa', 'address': '26 Plam street', 'phone': '676767676', 'status': 'PREPARING'},
    {'name': 'Richard', 'address': 'Down with surveillance!!!!!!', 'phone': '00000', 'status': 'PREPARING'},
]


def main_menu():   
    choice = utilities.get_choice([
        'Exit program',
        'View products',
        'View orders',
    ])
    return choice


def product_menu():   
    choice = utilities.get_choice([
        'Return to main menu',
        'View products',
        'Add new product',
        'Update product',
        'Delete product',
    ])
    return choice
  

def order_menu():
    choice =utilities.get_choice([
        'Return to main menu',
        'Show orders',
        'Add order',
        'Update order status',
        'Update items in the order',
        'Delete order',
    ])
    return choice


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
               
   
