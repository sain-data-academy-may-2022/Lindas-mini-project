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

    order['items'] = utilities.get_int_choices(products, 'Please select products to add to the order separated by commas: ')
        
    courier_num = utilities.get_choice(couriers)
    order['courier'] = courier_num

    orders.append(order)
    utilities.write_json('orders.json', orders)


# Updating orders status

def order_status(orders):
    order_num = utilities.get_choice(orders)
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

def update_order(orders, products, couriers):
    order_num = utilities.get_choice(orders)
    car = orders[order_num].items()
    for (key,value) in car:
        if key == 'status':
            continue
        elif key == 'items':
            new_items = utilities.get_int_choices(products, 'Please write updated items: ', True)
            if len(new_items) != 0:
                orders[order_num][key] = new_items
        elif key == 'courier':
            new_value = utilities.get_choice(couriers, True)
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
    