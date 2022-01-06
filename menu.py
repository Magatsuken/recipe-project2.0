import database


def display_main_menu():
    print("1. View all recipes")
    print("2. Search for a recipe")
    print("3. Add a recipe")
    print("4. Quit app")


def main_menu_input():
    valid = ['1', '2', '3', '4']
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


