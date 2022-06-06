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

def get_choice(list, allow_blank = False):
    print_list(list)
    while True:
        new_choice = input('Please select item: ')
        if allow_blank == True and new_choice == '':
            return ''
        try:
            which_item = int(new_choice) -1
            if which_item < 0 or which_item >= len(list):
                print('Please select a valid number')
            else:
                return which_item
        except ValueError:
            print('Please write a number')


# Turns choice str into list of ints

def get_int_choices(list, message, allow_blank = False):
    print_list(list)
    while True:
        try:   
            user_input = input(message).split(',')
            if allow_blank == True and user_input == ['']:
                return []

            items = []
            everything_ok = True

            for string in user_input:
                number = int(string) -1
                if number < 0 or number >= len(list):
                    everything_ok = False
                    break
                items.append(number)

            if everything_ok:
                return items
            else:
                print("Enter valid numbers!")
        except ValueError:
            print('Please enter a number!')


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
