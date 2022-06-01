import utilities


# Add order to the orders list
    
def add_order(orders, couriers, products):
    print('')
    order = {
        'name': input('Please enter customer name: '),
        'address': input('Please enter customer address: '),
        'phone': input('Please enter customer phone number: '),
        'status': 'PENDING',
        'items': [],
    }

    utilities.print_list(products)
    user_input = input('Please select products to add to the order: ').split(',')
    items = []
    for number in user_input:
        items.append(int(number))
    order['items'] = items

    courier_num = utilities.get_choice(couriers)
    order['courier'] = courier_num

    orders.append(order)
    utilities.write_json('orders.json', orders)


# Updating orders status

def order_status(orders):
    order_num = utilities.get_choice(orders)
    print('')
    print('1 - Pending')
    print('2 - Picking')
    print('3 - Preparing')
    print('4 - Dispatched')
    print('5 - Delivered')
    statuses = [
       'PENDING',
       'PICKING',
       'PREPARING',
       'DISPATCHED',
       'DELIVERED',
    ]
    status_num = utilities.get_choice(statuses)
    orders[order_num]['status'] = statuses[status_num]
    utilities.write_json('orders.json', orders)


# Updating order details

def update_order(orders):
    order_num = utilities.get_choice(orders)
    car = orders[order_num].items()
    for (key,value) in car:
        if key == 'status':
            continue
        new_value = input(f'Please write the new {key}: ')
        if new_value != '':
            orders[order_num][key]=new_value
    utilities.write_json('orders.json', orders)
            

# Deleting order from a list

def delete_order(list):
    num = utilities.get_choice(list)
    del list[num]
    utilities.write_json('orders.json', list)
    