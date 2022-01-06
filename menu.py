import database


def display_main_menu():
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
            print('Please enter a valid value.\n')
            display_main_menu()
            continue
        else:
            break
    main_menu_func(user_input)


def display_search_menu():
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
    print("1. Edit name")
    print("2. Edit cook time")
    print("3. Edit method")
    print("4. Edit ingredient")
    print("5. Edit preparation")
    print("6. Edit quantity")
    print("7. Edit instruction")


def edit_menu_input():
    valid = ['1', '2', '3', '4', '5', '6', '7']
    while True:
        try:
            user_input = input('Choose a number: ')
            if user_input not in valid:
                raise ValueError
        except ValueError:
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
        pass
    if user_input in '4':
        pass
    if user_input in '5':
        pass
    if user_input in '6':
        pass
    if user_input in '7':
        pass