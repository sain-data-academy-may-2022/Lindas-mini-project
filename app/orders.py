from dbfuncs import OrderManager
from dbfuncs import CourierManager
from dbfuncs import ProductManager
import utilities

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
    
    products = product_manager.get_all()
    product_indexes = utilities.get_int_choices(products, 'Please select products to add to the order separated by commas: ')
    product_ids = []
    for product_index in product_indexes:
        product_id = products[product_index]['id']
        product_ids.append(product_id)

        
    couriers = courier_manager.get_all()
    courier_idx = utilities.get_choice(couriers)
    courier_id = couriers[courier_idx]['id']

    order_manager.create(name, address, phone, status, product_ids, courier_id)



# Updating orders status

def order_status(order_manager: OrderManager, statuses):
    orders = order_manager.get_all()
    order_index = utilities.get_choice(orders, True)
    if order_index == '':
        print('Update cancelled!')
        return
    order_id = orders[order_index]['id']
    status_index = utilities.get_choice(statuses)
    order_manager.update_order_status(order_id, statuses[status_index])


# Updating order details

def update_order(order_manager: OrderManager, product_manager: ProductManager, courier_manager: CourierManager):
    orders = order_manager.get_all()
    order_index = utilities.get_choice(orders, True)
    if order_index == '':
        print('Update cancelled!')
        return
    order_id = orders[order_index]['id']
    customer_id = orders[order_index]['customer_id']

    for key in ['name', 'address', 'phone', 'courier']:
        # if key == 'items':
        #     products = product_manager.get_all()
        #     new_items = utilities.get_int_choices(products, 'Please write updated items: ', True)
        #     if len(new_items) != 0:
        #         # orders[order_num][key] = new_items
        #         pass
        if key == 'courier':
            couriers = courier_manager.get_all()
            courier_index = utilities.get_choice(couriers, True)
            if courier_index != '':

                courier_id = couriers[courier_index]['id']
                order_manager.update_courier(order_id, courier_id)

        elif key == 'name':
            name = input('Enter the new customer name: ')
            if name != '':
                order_manager.update_customer_name(customer_id, name) 
               
        elif key == 'address':
            address = input('Enter the new address: ')
            if address != '':
                order_manager.update_customer_address(customer_id, address)   
        
        elif key == 'phone':
            phone = input('Enter the new phone number: ')
            if phone !='':
                order_manager.update_customer_phone(customer_id, phone)


# Deleting order from a list

def delete_order(order_manager: OrderManager):
    orders = order_manager.get_all()
    index = utilities.get_choice(orders, True)
    if index == '':
        print('Delete cancelled!')
        return

    id = orders[index]['id']
    customer_id = orders[index]['customer_id']
    order_manager.delete_order(id, customer_id)
    print('Order deleted!')


# Sorting orders by delivery statuses

def sort_order_by_status(order_manager: OrderManager, statuses):
    status_index = utilities.get_choice(statuses, True)
    if status_index == '':
        print('Sorting cancelled!')
        return

    status = statuses[status_index]
    orders = order_manager.view_orders_by_status(status)
    utilities.print_list(orders)
    

# Sorting orders by courier

def sort_order_by_courier(order_manager: OrderManager, courier_manager: CourierManager):
    couriers = courier_manager.get_all()
    courier_num = utilities.get_choice(couriers, True)
    if courier_num == '':
        print('Sorting cancelled!')
        return

    courier_id = couriers[courier_num]['id']
    orders = order_manager.view_orders_by_courier(courier_id)
    utilities.print_list(orders)