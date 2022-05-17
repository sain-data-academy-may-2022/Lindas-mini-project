# function to get product choice from customer

def get_product_choice(list):
    print_list(list)
    while True:
        try:
            which_item = int(input('Please select item: ')) -1
            if which_item < 0 or which_item >= len(list):
                print('Please select a valid number')
            else:
                return which_item
        except ValueError:
            print('Please write a number')


# Prints the list of items with indexes

def print_list(items):
    print('')
    for (i, item) in enumerate(items, start = 1):
        print(i, item)


#  Adding new item to the product list

def add_item(list):
    new_item = input('Please enter new item: ')
    list.append(new_item)


#  Updating the item from product list

def update_item(list):
    num = get_product_choice(list)
    updated_item = input('Write the new item name: ')
    list[num] = updated_item
        

#  Deleting item from product list

def remove_item(list):
    num = get_product_choice(list)
    del list[num]
