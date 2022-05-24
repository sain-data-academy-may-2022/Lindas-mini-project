import utilities


# Add order to the orders list
    
def add_order(orders):
    print('')
    order = {
        'name': input('Please enter customer name: '),
        'address': input('Please enter customer address: '),
        'phone': input('Please enter customer phone number: '),
        'status': 'PENDING',
    }
    orders.append(order)


# Updating orders status

def order_status(orders):
    order_num = utilities.get_choice(orders)
    print('')
    print('1 - Pending')
    print('2 - Picking')
    print('3 - Preparing')
    print('4 - Dispatched')
    print('5 - Delivered')
    num = utilities.get_choice(orders)
    statuses = {
       1: 'PENDING',
       2: 'PICKING',
       3: 'PREPARING',
       4: 'DISPATCHED',
       5: 'DELIVERED',
    }
    orders[order_num]['status'] = statuses[num]


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

