from dbfuncs import ProductManager
import utilities



#  Adding new item to the product list

def add_item(product_manager: ProductManager):
    print('')
    name = input('Please enter new item: ')
    if name =='':
        print('Add cancelled!')
        return

    price = utilities.get_positive_float('Please select price for the new item: ')
    quantity = input('Please select the amount of items we have: ')
    product_manager.create(name, price, quantity)


#  Updating the item from product list

def update_item(product_manager: ProductManager):
    products = product_manager.get_all()
    product_num = utilities.get_choice(products, True)
    if product_num == '':
        print('Update cancelled!')
        return 

    product = products[product_num]
    for (key,value) in product.items():
        if key == "id":
            continue
        new_value = input(f'Please write the new {key}: ')
        if new_value != '':
            if key == 'price':
                new_value = float(new_value)
            product[key] = new_value
    product_manager.update(product["id"], product["name"], product["price"], product["quantity"])
            
        
#  Deleting item from a list

def delete_product(product_manager: ProductManager):
    list = product_manager.get_all()
    num = utilities.get_choice(list, True)
    if num  == '':
        print('Delete cancelled!')
        return 

    id = list[num]['id']
    product_manager.delete(id)
    print('Product deleted!')
    
    