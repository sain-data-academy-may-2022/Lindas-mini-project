from courier_manager import CourierManager
import utilities

 
# Adding new courier

def add_courier(courier_manager: CourierManager):
    print('')
    name = input('Please enter new courier: ')
    if name == '':
        print('Add cancelled!')
        return

    phone = utilities.get_string('Please put in phone number: ')
    courier_manager.create(name, phone)


# Updating courier name

def update_courier(courier_manager: CourierManager):
    couriers = courier_manager.get_all()
    courier = utilities.get_choice(couriers, True)
    if not courier:
        print('Update cancelled!')
        return 

    for (key,value) in courier.items():
        if key == "id":
            continue
        new_value = input(f'Please write the new {key}: ')
        if new_value != '':
            courier[key] = new_value
    courier_manager.update(courier["id"], courier["name"], courier["phone"])


# Deleting order from a list

def delete_courier(courier_manager: CourierManager):
    couriers = courier_manager.get_all()
    courier = utilities.get_choice(couriers, True)
    if not courier:
        print('Delete canceled!')
        return

    courier_manager.delete(courier["id"])
    print('Courier deleted!')