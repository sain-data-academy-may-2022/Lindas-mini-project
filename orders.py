# Print order list

def print_orders(orders):
    print('')
    for (o, order) in enumerate(orders, start = 1):
        print(o, order)


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
    print_orders(orders)
    order_num = int(input('Please choose and order to be updated: '))
    print('')
    print('1 - Pending')
    print('2 - Picking')
    print('3 - Preparing')
    print('4 - Dispatched')
    print('5 - Delivered')
    num = int(input('Select order status: '))
    statuses = {
       1: 'PENDING',
       2: 'PICKING',
       3: 'PREPARING',
       4: 'DISPATCHED',
       5: 'DELIVERED',
    }
    orders[order_num-1]['status'] = statuses[num]


# Updating order details

def update_order(orders):
    print_orders(orders)
    order_num = int(input('Please choose and order to be updated: '))
    car = orders[order_num -1].items()
    for (key,value) in car:
        if key == 'status':
            continue
        new_value = input(f'Please write the new {key}: ')
        if new_value != '':
            orders[order_num -1][key]=new_value


# Deleting order

def remove_order(orders):    
    print_orders(orders)
    num = int(input('Please select order to be deleted: '))
    del orders[num -1]

