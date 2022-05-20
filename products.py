import utilities


#  Adding new item to the product list

def add_item(list):
    new_item = input('Please enter new item: ')
    list.append(new_item)


#  Updating the item from product list

def update_item(list):
    num = utilities.get_choice(list)
    updated_item = input('Write the new item name: ')
    list[num] = updated_item
        

#  Deleting item from product list

def remove_item(list):
    num = utilities.get_choice(list)
    del list[num]
