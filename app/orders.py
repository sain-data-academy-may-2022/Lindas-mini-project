from typing import List
from order_manager import OrderManager
from courier_manager import CourierManager
from product_manager import ProductManager
import utilities


def view_orders(order_manager: OrderManager):
    orders = order_manager.get_all()
    print_orders(orders)


def print_orders(orders: List):
    utilities.print_list(orders, ['id', 'courier_id', 'customer_id'])


# Add order to the orders list
    
def add_order(courier_manager: CourierManager, product_manager: ProductManager, order_manager:OrderManager):
    print('')
    name = input('Please enter customer name: ')
    if name == '':
        print('Add cancelled!')
        return

    address = utilities.get_string('Please enter customer address: ')
    phone = utilities.get_string('Please enter customer phone number: ')
    status = 'PENDING'
    
    product_ids = get_product_choices(product_manager, 'Please select products to add to the order separated by commas: ', False)

    couriers = courier_manager.get_all()
    courier = utilities.print_list_and_get_choice(couriers)

    order_manager.create(name, address, phone, status, product_ids, courier['id'])


# Updating orders status

def order_status(order_manager: OrderManager, statuses):
    orders = order_manager.get_all()
    print_orders(orders)
    order = utilities.get_choice(orders, True)
    if not order:
        print('Update cancelled!')
        return
    order_id = order['id']
    status = utilities.print_list_and_get_choice(statuses)
    order_manager.update_order_status(order_id, status)


# Updating order details

def update_order(order_manager: OrderManager, product_manager: ProductManager, courier_manager: CourierManager):
    orders = order_manager.get_all()
    print_orders(orders)
    order = utilities.get_choice(orders, True)
    if not order:
        print('Update cancelled!')
        return

    order_id = order['id']
    customer_id = order['customer_id']

    name = input('Enter the new customer name: ')
    if name != '':
        order_manager.update_customer_name(customer_id, name) 

    address = input('Enter the new address: ')
    if address != '':
        order_manager.update_customer_address(customer_id, address)

    phone = input('Enter the new phone number: ')
    if phone !='':
        order_manager.update_customer_phone(customer_id, phone)

    product_ids = get_product_choices(product_manager, 'Enter new product choices separated by commas: ', True)
    if product_ids != []:
        order_manager.update_products(order_id, product_ids)

    couriers = courier_manager.get_all()
    courier = utilities.print_list_and_get_choice(couriers, True)
    if courier:
        order_manager.update_courier(order_id, courier['id'])


# Deleting order from a list

def delete_order(order_manager: OrderManager):
    orders = order_manager.get_all()
    print_orders(orders)
    order = utilities.get_choice(orders, True)
    if not order:
        print('Delete cancelled!')
        return

    order_manager.delete_order(order['id'], order['customer_id'])
    print('Order deleted!')


# Sorting orders by delivery statuses

def sort_order_by_status(order_manager: OrderManager, statuses):
    status = utilities.print_list_and_get_choice(statuses, True)
    if not status:
        print('Sorting cancelled!')
        return

    orders = order_manager.view_orders_by_status(status)
    print_orders(orders)
    

# Sorting orders by courier

def sort_order_by_courier(order_manager: OrderManager, courier_manager: CourierManager):
    couriers = courier_manager.get_all()
    courier = utilities.print_list_and_get_choice(couriers, True)
    if not courier:
        print('Sorting cancelled!')
        return

    orders = order_manager.view_orders_by_courier(courier['id'])
    print_orders(orders)


def get_product_choices(product_manager, message, allow_blank):
    products = product_manager.get_all()
    utilities.print_list(products)
    product_indexes = utilities.get_int_choices(products, message, allow_blank)
    product_ids = []
    for product_index in product_indexes:
        product_id = products[product_index]['id']
        product_ids.append(product_id)
    return product_ids