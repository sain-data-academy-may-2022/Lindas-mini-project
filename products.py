import utilities


#  Adding new item to the product list

def add_item(list):
    print('')
    product = {
        'product': input('Please enter new item: '),
        'price': utilities.get_positive_float('Please select price for the new item: ')
    }
    list.append(product)
    utilities.write_json('products.json', list)


#  Updating the item from product list

def update_item(products):
    product_num = utilities.get_choice(products)
    car = products[product_num].items()
    for (key,value) in car:
        new_value = input(f'Please write the new {key}: ')
        if new_value != '':
            if key == 'price':
                new_value = float(new_value)
            products[product_num][key]=new_value
    utilities.write_json('products.json', products)
            
        
#  Deleting item from a list

def delete_product(list):
    num = utilities.get_choice(list)
    del list[num]
    utilities.write_json('products.json', list)
    