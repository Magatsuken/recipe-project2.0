import database
import os


def display_main_menu():
    os.system('cls')
    print("1. View all recipes")
    print("2. Search for a recipe")
    print("3. Add a recipe")
    print("4. Delete a recipe")
    print("5. Edit an entry")
    print("6. Quit App")


def main_menu_input():
    valid = ['1', '2', '3', '4', '5', '6']
    while True:
        try:
            user_input = input('Choose a number: ')
            if user_input not in valid:
                raise ValueError
        except ValueError:
            os.system('cls')
            print('Please enter a valid value.\n')
            display_main_menu()
            continue
        else:
            break
    main_menu_func(user_input)


def display_search_menu():
    os.system('cls')
    print("1. Search by name")
    print("2. Search by ingredients")
    print("3. Search by cook time")
    print("4. Search by method")
    print("5. Back to previous menu")


def search_menu_input():
    valid = ['1', '2', '3', '4', '5']
    while True:
        try:
            user_input = input('Choose a number: ')
            if user_input not in valid:
                raise ValueError
        except ValueError:
            os.system('cls')
            print('Please enter a valid value.\n')
            display_search_menu()
            continue
        else:
            break
    search_menu_func(user_input)


def main_menu_func(user_input):
    if user_input in '1':
        database.show_all_recipe_names()
        database.select_recipe()
    if user_input in '2':
        display_search_menu()
        search_menu_input()
    if user_input in '3':
        database.create_new_recipe()
    if user_input in '4':
        database.delete_recipe()
    if user_input in '5':
        database.edit_entry()
    if user_input in '6':
        pass


def search_menu_func(user_input):
    if user_input in '1':
        database.search_by_name()
    if user_input in '2':
        database.search_by_ingredient()
    if user_input in '3':
        database.search_by_cook_time()
    if user_input in '4':
        database.search_by_method()
    if user_input in '5':
        display_main_menu()
        main_menu_input()


def display_edit_menu():
    os.system('cls')
    print("1. Edit name")
    print("2. Edit cook time")
    print("3. Edit method")
    print("4. Edit ingredient")
    print("5. Edit instruction")
    print("6. Back to previous menu")


def edit_menu_input():
    valid = ['1', '2', '3', '4', '5', '6']
    while True:
        try:
            user_input = input('Choose a number: ')
            if user_input not in valid:
                raise ValueError
        except ValueError:
            os.system('cls')
            print('Please enter a valid value.\n')
            display_edit_menu()
            continue
        else:
            break
    edit_menu_func(user_input)


def edit_menu_func(user_input):
    if user_input in '1':
        database.edit_name()
    if user_input in '2':
        database.edit_cook_time()
    if user_input in '3':
        database.edit_method()
    if user_input in '4':
        display_edit_ingredient_menu()
        edit_ingredient_menu_input()
    if user_input in '5':
        display_edit_instruction_menu()
        edit_instruction_menu_input()
    if user_input in '6':
        display_main_menu()
        main_menu_input()


def display_edit_ingredient_menu():
    os.system('cls')
    print("1. Edit a current entry")
    print("2. Add an ingredient to an entry")
    print("3. Remove an ingredient from an entry")


def edit_ingredient_menu_input():
    valid = ['1', '2', '3']
    while True:
        try:
            user_input = input('Choose a number: ')
            if user_input not in valid:
                raise ValueError
        except ValueError:
            os.system('cls')
            print('Please enter a valid value.\n')
            display_edit_ingredient_menu()
            continue
        else:
            break
    edit_ingredient_menu_func(user_input)


def edit_ingredient_menu_func(user_input):
    if user_input == '1':
        database.edit_ingredient()
    if user_input == '2':
        database.add_ingredient()
    if user_input == '3':
        database.remove_ingredient()


def display_edit_instruction_menu():
    os.system('cls')
    print("1. Edit a current entry")
    print("2. Add an instruction to an entry")
    print("3. Remove an instruction from an entry")


def edit_instruction_menu_input():
    valid = ['1', '2', '3']
    while True:
        try:
            user_input = input('Choose a number: ')
            if user_input not in valid:
                raise ValueError
        except ValueError:
            os.system('cls')
            print('Please enter a valid value.\n')
            display_edit_instruction_menu()
            continue
        else:
            break
    edit_instruction_menu_func(user_input)


def edit_instruction_menu_func(user_input):
    if user_input == '1':
        database.edit_instruction()
    if user_input == '2':
        database.add_instruction()
    if user_input == '3':
        database.remove_instruction()