#!/usr/bin/env python3


# Put my_list before the functions definitions, beneath this comment
my_list = [1, 2, 3, 4, 5]



def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    new_item = ordered_list[-1] + 1
    ordered_list.append(new_item)

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values found in items_to_remove list from ordered_list
    for item in items_to_remove:
        while item in ordered_list:  # Make sure that every occurrence is eliminated
            ordered_list.remove(item)

# The primary code
if __name__ == '__main__':
    print(my_list)  # Initial list
    add_item_to_list(my_list)  # Item to add
    add_item_to_list(my_list)  # Item to add
    add_item_to_list(my_list)  # Item to add
    print(my_list)  # List after additions
    remove_items_from_list(my_list, [1, 5, 6])  # Remove specified items
    print(my_list)  # Final list





