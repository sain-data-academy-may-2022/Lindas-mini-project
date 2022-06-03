import json


# imports from json

def import_json(filename):
    try:
        with open(filename) as file:
            return json.load(file)
    except:
        return []


# overrides the json file with new items

def write_json(filename, list):
    with open(filename, 'w') as file:
        json.dump(list, file, indent = 4)   
    

# Prints the list of items with indexes

def print_list(items):
    print('')
    if not items:
        print('No Items!')
    else:
        for (i, item) in enumerate(items, start = 1):
            print(i, item)


# function to check if imput is safe

def get_choice(list):
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


# Checks if input is a positive float

def get_positive_float(message):
    while True:
        try:
            num = float(input(message))
            if num <= 0:
                print('Please select a positive number')
            else:
                return num
        except ValueError:
            print('Please write a number')


# Checks if input is a positive number or zero

def get_positive_int_or_zero(message):
    while True:
        try:
            num = int(input(message))
            if num < 0:
                print('Please select a positive number')
            else:
                return num
        except ValueError:
            print('Please write a number')
