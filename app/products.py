from dbfuncs import ProductManager
import utilities



#  Adding new item to the product list

def add_item(product_manager: ProductManager):
    print('')
    name = input('Please enter new item: ')
    price = utilities.get_positive_float('Please select price for the new item: ')
    product_manager.create(name, price)


#  Updating the item from product list

def update_item(product_manager: ProductManager):
    products = product_manager.get_all()
    product_num = utilities.get_choice(products)
    product = products[product_num]

    car = product.items()
    for (key,value) in car:
        if key == "ID":
            continue
        new_value = input(f'Please write the new {key}: ')
        if new_value != '':
            if key == 'price':
                new_value = float(new_value)
            product[key] = new_value
    product_manager.update(product["ID"], product["Name"], product["Price"])
            
        
#  Deleting item from a list

def delete_product(product_manager: ProductManager):
    list = product_manager.get_all()
    num = utilities.get_choice(list)
    id = list[num]['ID']
    product_manager.delete(id)
    
    