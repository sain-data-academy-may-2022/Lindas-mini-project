from typing import Dict, List
from prettytable import PrettyTable
import os


# Prints the list of items with indexes

def print_list(rows, without_keys=['id']):
    print('')
    if bool(rows) == False:
        print('No Items!')
        return
    
    first = rows[0]
    if type(first) is dict:
        x = PrettyTable()
        x.field_names = ['Num'] + list(dict_without(first, without_keys).keys())
        for (i, row) in enumerate(rows, start = 1):
            x.add_row([i] + list(dict_without(row, without_keys).values()))
        print(x)
    else:
        for (i, row) in enumerate(rows, start = 1):
            print(f'[{i}] - {row}')


# function to check if imput is safe

def print_list_and_get_choice(items: List, allow_blank = False):
    print_list(items)
    return get_choice(items, allow_blank)

def get_choice(items: List, allow_blank = False):
    while True:
        new_choice = input('Please select item: ')
        if allow_blank == True and new_choice == '':
            return None
        try:
            which_item = int(new_choice) - 1
            if which_item < 0 or which_item >= len(items):
                print('Please select a valid number')
            else:
                return items[which_item]
        except ValueError:
            print('Please write a number')


# Turns choice str into list of ints

def get_int_choices(list, message, allow_blank = False):
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


# function to check if input is safe string

def get_string(message):
    while True:
        new_string = input(message)
        if new_string == '':
            print('Please enter a value')
        elif len(new_string) > 255:
            print('Its too long!')
        else:
            return new_string


# Checks if input is a positive float

def get_positive_float(message, allow_blank = False):
    while True:
        try:
            user_input = input(message) 
            if allow_blank == True and user_input == '':
                return None
            
            user_input = float(user_input)
            if user_input <= 0:
                print('Please select a positive number')
            else:
                return user_input
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


def clear_screen():
    os.system('clear')


def dict_without(dict: Dict, without_keys: List):
    new_dict = {}
    for (key, value) in dict.items():
        if key not in without_keys:
            new_dict[key] = value
    return new_dict


def list_of_dicts_without(rows: List, without_keys: List):
    new_list = []
    for row in rows:
        new_dict = dict_without(row, without_keys)
        new_list.append(new_dict)
    return new_list