import utilities

 
# Adding new courier

def add_courier(couriers):
    print('')
    courier_list = {
        'name': input('Please enter new courier: '),
        'phone': input('Please put in phone number: ')
    }
    couriers.append(courier_list)
    utilities.write_json('couriers.json', couriers)


# Updating courier name

def update_courier(list):
    num = utilities.get_choice(list)
    updated_item = input('Write the new courier name: ')
    list[num] = updated_item
    utilities.write_json('couriers.json', list)


# Deleting order from a list

def delete_courier(list):
    num = utilities.get_choice(list)
    del list[num]
    utilities.write_json('couriers.json', list)
    