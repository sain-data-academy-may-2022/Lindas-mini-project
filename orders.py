# Print order list

def print_order(orders):
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
        'status': 'PREPARING',
    }
    orders.append(order)


# Updating orders status

def order_status(orders):
    print('')
    print('1 - Pending')
    print('2 - Picking')
    print('3 - Asembling')
    print('4 - Dispatched')
    print('5 - Delivered')

