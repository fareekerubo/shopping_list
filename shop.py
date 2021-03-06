import os
import sys


shoppingList = []


def instructions():
    print("What should we pick up at the shops?")
    print("""
You have {} items in your list.
Enter HELP to show this help menu again.
Enter SHOW to see your list.
Enter REMOVE to remoeve an item.
Enter CLEAR to delete your list.
Enter SAVE to save your list and exit."""))


def print_shopping_list():
    print("-----------------------")
    print("Shopping List")
    for item in shoppingList:
        print(">" + item)

def add_item_to_list(item):
    shoppingList.append(item)
    print("-------------------------------------------------------")
    print("Added {} to shopping list! List now has {} items".format(item, len(shoppingList)))



def main():   
    instructions()
    while True:
        item = str(input("Enter an item to add to the list... "))
        if item == 'DONE':
            print_shopping_list()
            break
        elif item == 'SHOW':
            print_shopping_list()
        elif item == 'HELP':
            help_instruc()
        else:
            add_item_to_list(item)
            
main()
