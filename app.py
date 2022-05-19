import products
import orders

my_products = ['Pepper up', 'Draught of Peace', 'Amorentia', 'Fatigue Infusion', 'Invisibility potion']
my_orders = []

def main_menu():   
    print('') 
    print('1 - Exit program')
    print('2 - View products')
    print('3 - View orders')

    choice = input('Please select an option: ')
    return choice

def product_menu():   
    print('') 
    print('1 - Return to main menu')
    print('2 - View products')
    print('3 - Add new product')
    print('4 - Update product')
    print('5 - Delete product')

    choice = input('Please select an option: ')
    return choice

def order_menu():
    print('')
    print('1 - Return to main menu')
    print('2 - Show orders')
    print('3 - Customer information')
    print('4 - Update order status')
    print('5 - Update items in the order')
    print('6 - Delete order')

    choice = input('Please select an option: ')
    return choice


while True:
    choice = main_menu()
    if choice == '1':
        break
    elif choice == '2':
        while True:
            choice = product_menu()
            if choice == '1':
                break
            elif choice == '2':
                products.print_list(my_products)
            elif choice == '3':
                products.add_item(my_products)
            elif choice == '4':
                products.update_item(my_products)
            elif choice == '5':
                products.remove_item(my_products)
    elif choice == '3':
        while True:
            choice = order_menu()
            if choice == '1':
                break
            elif choice == '2':
                orders.print_order(my_orders)
            elif choice == '3':
                orders.add_order(my_orders)
            elif choice == '4':
                orders.order_status(my_orders)
            elif choice == '5':
                print('my_order')
