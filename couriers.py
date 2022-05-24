import utilities

 
# Adding new courier

def add_courier(courier):
    new_item = input('Please enter new courier: ')
    courier.append(new_item)


# Updating courier name

def update_courier(list):
    num = utilities.get_choice(list)
    updated_item = input('Write the new courier name: ')
    list[num] = updated_item


# Deleting order from a list

def delete_courier(list):
    num = utilities.get_choice(list)
    del list[num]
    utilities.write_json('couriers.json', list)
    