# Prints the list of items with indexes

def print_list(items):
    print('')
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