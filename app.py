import products

my_products = ['Pepper up', 'Draught of Peace', 'Amorentia', 'Fatigue Infusion', 'Invisibility potion']


def main_menu():   
    print('') 
    print('1 - Exit program')
    print('2 - View products')
    print('3 - View orders')

    choice = input('Please select an option: ')
    return choice

def product_menu():   
    print('') 
    print('1 - Exit')
    print('2 - View products')
    print('3 - Add new product')
    print('4 - Update product')
    print('5 - Delete product')

    choice = input('Please select an option: ')
    return choice

def order_menu():
    print('')
    print('1 - Exit')
    print('2 - Order')
    print('3 - Update order status')
    print('4 - Update items in the order')
    print('5 - Delete order')

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
                print('my_order')
            elif choice == '3':
                print('my_order')
            elif choice == '4':
                print('my_order')
            elif choice == '5':
                print('my_order')
