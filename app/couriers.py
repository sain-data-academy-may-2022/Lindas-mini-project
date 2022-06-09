from dbfuncs import CourierManager
import utilities

 
# Adding new courier

def add_courier(courier_manager: CourierManager):
    print('')
    name = input('Please enter new courier: '),
    phone =  input('Please put in phone number: ')
    courier_manager.create(name, phone)


# Updating courier name

def update_courier(courier_manager: CourierManager):
    couriers = courier_manager.get_all()
    courier_num = utilities.get_choice(couriers)
    courier = couriers[courier_num]

    car = courier.items()
    for (key,value) in car:
        if key == "ID":
            continue
        new_value = input(f'Please write the new {key}: ')
        if new_value != '':
            courier[key] = new_value
    courier_manager.update(courier["ID"], courier["Name"], courier["Phone"])

# Deleting order from a list

def delete_courier(courier_manager: CourierManager):
    list = courier_manager.get_all()
    num = utilities.get_choice(list)
    id = list[num]["ID"]
    courier_manager.delete(id)