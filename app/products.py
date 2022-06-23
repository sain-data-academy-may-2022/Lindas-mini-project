from typing import List
from product_manager import ProductManager
import utilities



#  Adding new item to the product list

def add_item(product_manager: ProductManager):
    print('')
    name = input('Please enter new item: ')
    if name == '':
        print('Add cancelled!')
        return

    price = utilities.get_positive_float('Please select price for the new item: ')
    product_manager.create(name, price)


#  Updating the item from product list

def update_item(product_manager: ProductManager):
    products = product_manager.get_all()
    product = utilities.get_choice(products, True)
    if not product:
        print('Update cancelled!')
        return 

    for (key,value) in product.items():
        if key == "id":
            continue
        if key == 'price':
            new_value = utilities.get_positive_float(f'Please write the new {key}: ', True)
        else:
            new_value = input(f'Please write the new {key}: ')
        if new_value:
            product[key] = new_value
    product_manager.update(product["id"], product["name"], product["price"])
            
        
#  Deleting item from a list

def delete_product(product_manager: ProductManager):
    products = product_manager.get_all()
    product = utilities.get_choice(products, True)
    if not product:
        print('Delete cancelled!')
        return 

    product_manager.delete(product['id'])
    print('Product deleted!')