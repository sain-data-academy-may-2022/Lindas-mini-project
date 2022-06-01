import products
import orders
import couriers
import utilities

my_products = utilities.import_json('products.json')   
my_orders = utilities.import_json('orders.json')
my_couriers = utilities.import_json('couriers.json')


def main_menu():  
    return utilities.get_choice([
        'Leave this place!',
        'Products',
        'Orders',
        'Couriers',
    ])
    

def product_menu():   
    return utilities.get_choice([
        'Pack up to leave',
        'View products',
        'Add new product',
        'Update product',
        'Delete product',
    ])
 

def order_menu():
    return utilities.get_choice([
        'Pack up to leave',
        'Show orders',
        'Add order',
        'Update order status',
        'Update items in the order',
        'Delete order',
    ])


def courier_menu():
    return utilities.get_choice([
        'Pack up to leave',
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
                products.delete_product(my_products)
    elif choice == 2:
        while True:
            choice = order_menu()
            if choice == 0:
                break
            elif choice == 1:
                utilities.print_list(my_orders)
            elif choice == 2:
                orders.add_order(my_orders, my_couriers, my_products)
            elif choice == 3:
                orders.order_status(my_orders)
            elif choice == 4:
                orders.update_order(my_orders)
            elif choice == 5:
                orders.delete_order(my_orders)
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
                couriers.delete_courier(my_couriers)
                