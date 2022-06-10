from dbfuncs import CourierManager
from dbfuncs import ProductManager
import utilities

# Add order to the orders list
    
def add_order(orders, courier_manager: CourierManager, product_manager: ProductManager):
    print('')
    order = {
        'name': input('Please enter customer name: '),
        'address': input('Please enter customer address: '),
        'phone': input('Please enter customer phone number: '),
        'status': 'PENDING',
        'items': [],
    }
    products = product_manager.get_all()
    order['items'] = utilities.get_int_choices(products, 'Please select products to add to the order separated by commas: ')
        
    couriers = courier_manager.get_all()
    order['courier'] = utilities.get_choice(couriers)

    orders.append(order)
    utilities.write_json('orders.json', orders)


# Updating orders status

def order_status(orders, statuses):
    order_num = utilities.get_choice(orders)
    status_num = utilities.get_choice(statuses)
    orders[order_num]['status'] = statuses[status_num]
    utilities.write_json('orders.json', orders)


# Updating order details

def update_order(orders, product_manager: ProductManager, courier_manager: CourierManager):
    order_num = utilities.get_choice(orders)
    car = orders[order_num].items()
    for (key,value) in car:
        if key == 'status':
            continue
        elif key == 'items':
            products = product_manager.get_all()
            new_items = utilities.get_int_choices(products, 'Please write updated items: ', True)
            if len(new_items) != 0:
                orders[order_num][key] = new_items
        elif key == 'courier':
            courier = courier_manager.get_all()
            new_value = utilities.get_choice(courier, True)
            if new_value != '':
                orders[order_num][key]= new_value
        else:
            new_value = input(f'Please write the new {key}: ')
            if new_value != '':
                orders[order_num][key]= new_value
    utilities.write_json('orders.json', orders)
            

# Deleting order from a list

def delete_order(list):
    num = utilities.get_choice(list)
    del list[num]
    utilities.write_json('orders.json', list)


# Sorting orders by delivery statuses

def sort_order_by_status(orders, statuses):
    filtered = []
    status_num = utilities.get_choice(statuses)
    status = statuses[status_num]
    for order in orders:
        if order["status"] == status:
            filtered.append(order)
    utilities.print_list(filtered)
    

# Sorting orders by courier

def sort_order_by_courier(orders, courier_manager: CourierManager):
    filtered = []
    couriers = courier_manager.get_all()
    courier_num = utilities.get_choice(couriers)
    for order in orders:
        if order["courier"] == courier_num:
            filtered.append(order)
    utilities.print_list(filtered)