from tabulate import tabulate
import mysql.connector
from recipe import Recipe
import menu

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='recipedb'
)

mycursor = db.cursor()


def show_all_recipe_names():
    mycursor.execute('SELECT recipe_id, name FROM recipe')
    result = mycursor.fetchall()
    print(tabulate(result, headers=['ID', 'Name'], tablefmt='psql'))


def select_recipe():
    while True:
        try:
            user_input = input('Please type an ID #: ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE recipe_id IN ('%s')" % (user_input))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type a valid ID #! ')
            show_all_recipe_names()
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe.recipe_id in ('%s')" % (user_input))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE recipe.recipe_id in ('%s')" % (user_input))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    menu.display_main_menu()
    menu.main_menu_input()


def search_by_name():
    while True:
        try:
            user_input = input('Please type a recipe name: ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE name IN ('%s')" % (user_input))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type the full recipe name! ')
            show_all_recipe_names()
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE name in ('%s')" % (user_input))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE name in ('%s')" % (user_input))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    menu.display_main_menu()
    menu.main_menu_input()


def search_by_ingredient():
    while True:
        try:
            user_input = input('Please type an ingredient: ')
            mycursor.execute("SELECT recipe.recipe_id, name, cook_time, method FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE ingredients.ingredient in ('%s')" % (user_input))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please choose another ingredient! ')
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    while True:
        try:
            id_num = input('Please type an ID #: ')
            mycursor.execute(
                "SELECT recipe_id, name, cook_time, method FROM recipe WHERE recipe_id IN ('%s')" % (id_num))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type a valid ID #! ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe_id in ('%s')" % (id_num))
            result = mycursor.fetchall()
            print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    menu.display_main_menu()
    menu.main_menu_input()


def search_by_cook_time():
    while True:
        try:
            user_input = float(input('Please type how much time in hours: '))
            if user_input < 0:
                raise ValueError
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE cook_time <= ('%s')" % (user_input))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please try another cook time! ')
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    while True:
        try:
            id_num = input('Please type an ID #: ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE recipe_id IN ('%s')" % (id_num))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type a valid ID #! ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe_id in ('%s')" % (id_num))
            result = mycursor.fetchall()
            print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    menu.display_main_menu()
    menu.main_menu_input()


def search_by_method():
    while True:
        try:
            user_input = input('Please type a cooking method: ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE method IN ('%s')" % (user_input))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please try another cooking method! ')
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    while True:
        try:
            id_num = input('Please type an ID #: ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE recipe_id IN ('%s')" % (id_num))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type a valid ID #! ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe_id in ('%s')" % (id_num))
            result = mycursor.fetchall()
            print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    menu.display_main_menu()
    menu.main_menu_input()


def create_new_recipe():
    global recipe_id
    recipe_name = input('What is the recipe name? ')
    recipe_cook_time = input('What is the cook time in hours? ')
    recipe_method = input('What is the cooking method? ')

    recipe_ingredient = ''
    step_counter = 1
    ingredient_list = []
    ingredient_prep = []
    quantity_list = []
    while recipe_ingredient != 'done':
        recipe_ingredient = input('What is ingredient #%s? Type "done" if done. ' % (step_counter))
        ingredient_list.append(recipe_ingredient)
        if recipe_ingredient != 'done':
            recipe_prep = input('How do you prepare this? Do not input anything if no prep needed. ')
            if recipe_prep == '':
                ingredient_prep.append('')
            else:
                ingredient_prep.append(recipe_prep)
            quantity = input('How many ingredients do you use? IE 6 slices, 2 breasts. ')
            if quantity == '':
                quantity_list.append('')
            else:
                quantity_list.append(quantity)
        step_counter += 1
    ingredient_list.pop()

    recipe_instruction = ''
    step_counter = 1
    instruction_list = []
    while recipe_instruction != 'done':
        recipe_instruction = input('What is step #%s? Type "done" if done. ' % (step_counter))
        instruction_list.append(recipe_instruction)
        step_counter += 1
    instruction_list.pop()

    new_recipe = Recipe(recipe_name, recipe_cook_time, recipe_method, ingredient_list, ingredient_prep, quantity_list, instruction_list)
    print(new_recipe)

    mycursor.execute("INSERT INTO recipe (name, cook_time, method) VALUES ('%s', '%s', '%s')" % (new_recipe.name, new_recipe.cook_time, new_recipe.method))

    mycursor.execute("SELECT recipe_id FROM recipe ORDER BY recipe_id DESC LIMIT 1")
    result = mycursor.fetchone()
    for x in result:
        recipe_id = x

    print(len(new_recipe.ingredients))
    print(new_recipe.ingredients)
    print(new_recipe.preparation)
    print(new_recipe.quantity)
    for i in range(0, len(new_recipe.ingredients)):
        ingredient = new_recipe.ingredients[i]
        preparation = new_recipe.preparation[i]
        quantity = new_recipe.quantity[i]
        mycursor.execute("INSERT INTO ingredients(recipe_id, ingredient, preparation, quantity) VALUES ('%s', '%s', '%s', '%s')" % (recipe_id, ingredient, preparation, quantity))

        db.commit()

    instruction_num = 1
    for instruction in new_recipe.instructions:
        mycursor.execute("INSERT INTO instructions(recipe_id, instruction_num, instruction) VALUES ('%s', '%s', '%s')" % (recipe_id, instruction_num, instruction))
        instruction_num += 1

    db.commit()

    menu.display_main_menu()
    menu.main_menu_input()


def delete_recipe():
    while True:
        try:
            show_all_recipe_names()
            user_input = input('Please type a recipe name to delete: ')
            mycursor.execute("SELECT name, cook_time, method FROM recipe WHERE name IN ('%s')" % (user_input))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type the full recipe name! ')
            show_all_recipe_names()
            continue
        else:
            break
    mycursor.execute("SELECT recipe_id FROM recipe WHERE name='%s'" % (user_input))
    result = mycursor.fetchone()
    for x in result:
        recipe_id = x
    mycursor.execute("DELETE FROM instructions WHERE recipe_id='%s'" % recipe_id)
    mycursor.execute("DELETE FROM ingredients WHERE recipe_id='%s'" % (recipe_id))
    mycursor.execute("DELETE FROM recipe WHERE name='%s'" % (user_input))
    db.commit()

    menu.display_main_menu()
    menu.main_menu_input()


def edit_entry():
    menu.display_edit_menu()
    menu.edit_menu_input()


def edit_name():
    while True:
        try:
            show_all_recipe_names()
            id_num = input('Please type the ID of the recipe that you want to edit: ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE recipe.recipe_id IN ('%s')" % (id_num))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type a valid ID #! ')
            show_all_recipe_names()
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    new_name = input('What do you want the new name to be? ')
    mycursor.execute("UPDATE recipe SET name = '%s' WHERE recipe.recipe_id IN ('%s')" % (new_name, id_num))
    db.commit()

    menu.display_main_menu()
    menu.main_menu_input()


def edit_cook_time():
    while True:
        try:
            show_all_recipe_names()
            id_num = input('Please type the ID of the recipe that you want to edit: ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE recipe.recipe_id IN ('%s')" % (id_num))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type a valid ID #! ')
            show_all_recipe_names()
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    new_cook_time = input('What do you want the new cook time to be in hours? ')
    mycursor.execute("UPDATE recipe SET cook_time = '%s' WHERE recipe.recipe_id IN ('%s')" % (new_cook_time, id_num))
    db.commit()

    menu.display_main_menu()
    menu.main_menu_input()


def edit_method():
    while True:
        try:
            show_all_recipe_names()
            id_num = input('Please type the ID of the recipe that you want to edit: ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE recipe.recipe_id IN ('%s')" % (id_num))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type a valid ID #! ')
            show_all_recipe_names()
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    new_method = input('What do you want the new method to be? ')
    mycursor.execute("UPDATE recipe SET method = '%s' WHERE recipe.recipe_id IN ('%s')" % (new_method, id_num))
    db.commit()

    menu.display_main_menu()
    menu.main_menu_input()


def edit_ingredient():
    while True:
        try:
            show_all_recipe_names()
            id_num = input('Please type the ID of the recipe that you want to edit: ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE recipe.recipe_id IN ('%s')" % (id_num))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type a valid ID #! ')
            show_all_recipe_names()
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    while True:
        try:
            old_ingredient = input('Please type an ingredient: ')
            mycursor.execute("SELECT name, cook_time, method FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE ingredient in ('%s')" % (old_ingredient))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please choose another ingredient! ')
            continue
        else:
            break
    new_ingredient = input('What is the new ingredient? ')
    mycursor.execute("UPDATE ingredients SET ingredient = '%s' WHERE ingredient IN ('%s')" % (new_ingredient, old_ingredient))
    db.commit()
    new_preparation = input('How do you prepare this? Do not input anything if no prep needed. ')
    mycursor.execute("UPDATE ingredients SET preparation = '%s' WHERE ingredient IN ('%s')" % (new_preparation, new_ingredient))
    db.commit()
    new_quantity = input('How many ingredients do you use? IE 6 slices, 2 breasts. ')
    mycursor.execute("UPDATE ingredients SET quantity = '%s' WHERE ingredient IN ('%s')" % (new_quantity, new_ingredient))
    db.commit()

    menu.display_main_menu()
    menu.main_menu_input()


def add_ingredient():
    while True:
        try:
            show_all_recipe_names()
            id_num = input('Please type the ID of the recipe that you want to edit: ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE recipe.recipe_id IN ('%s')" % (id_num))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type a valid ID #! ')
            show_all_recipe_names()
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    new_ingredient = input('What is the new ingredient? ')
    new_preparation = input('How do you prepare this? Do not input anything if no prep needed. ')
    new_quantity = input('How many ingredients do you use? IE 6 slices, 2 breasts. ')

    mycursor.execute("INSERT INTO ingredients(recipe_id, ingredient, preparation, quantity) VALUES ('%s', '%s', '%s', '%s')" % (id_num, new_ingredient, new_preparation, new_quantity))
    db.commit()

    menu.display_main_menu()
    menu.main_menu_input()


def remove_ingredient():
    while True:
        try:
            show_all_recipe_names()
            id_num = input('Please type the ID of the recipe that you want to edit: ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE recipe.recipe_id IN ('%s')" % (id_num))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type a valid ID #! ')
            show_all_recipe_names()
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    while True:
        try:
            removed_ingredient = input('Please type an ingredient to remove: ')
            mycursor.execute("SELECT name, cook_time, method FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE ingredient in ('%s')" % (removed_ingredient))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please choose another ingredient! ')
            continue
        else:
            break
    mycursor.execute("DELETE FROM ingredients WHERE ingredient='%s' AND recipe_id='%s'" % (removed_ingredient, id_num))
    db.commit()

    menu.display_main_menu()
    menu.main_menu_input()


def edit_instruction():
    while True:
        try:
            show_all_recipe_names()
            id_num = input('Please type the ID of the recipe that you want to edit: ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE recipe.recipe_id IN ('%s')" % (id_num))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type a valid ID #! ')
            show_all_recipe_names()
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    while True:
        try:
            step_num = input('Please type a step number: ')
            mycursor.execute("SELECT instruction FROM instructions WHERE instruction_num in ('%s') AND recipe_id in ('%s')" % (step_num, id_num))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please choose a valid step! ')
            continue
        else:
            break
    new_instruction = input('What is the new instruction? ')
    mycursor.execute("UPDATE instructions SET instruction = '%s' WHERE instruction_num IN ('%s') AND recipe_id in ('%s')" % (new_instruction, step_num, id_num))
    db.commit()

    menu.display_main_menu()
    menu.main_menu_input()


def add_instruction():
    while True:
        try:
            show_all_recipe_names()
            id_num = input('Please type the ID of the recipe that you want to edit: ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE recipe.recipe_id IN ('%s')" % (id_num))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type a valid ID #! ')
            show_all_recipe_names()
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    new_instruction = input('What is the new instruction? ')

    mycursor.execute("SELECT instruction_num FROM instructions WHERE recipe_id='%s' ORDER BY instruction_num DESC LIMIT 1" % (id_num))
    result = mycursor.fetchone()
    if result == None:
        new_step = 0
    else:
        for x in result:
            new_step = int(x)

    new_step += 1
    mycursor.execute("INSERT INTO instructions(recipe_id, instruction_num, instruction) VALUES ('%s', '%s', '%s')" % (id_num, new_step, new_instruction))
    db.commit()

    menu.display_main_menu()
    menu.main_menu_input()


def remove_instruction():
    while True:
        try:
            show_all_recipe_names()
            id_num = input('Please type the ID of the recipe that you want to edit: ')
            mycursor.execute("SELECT recipe_id, name, cook_time, method FROM recipe WHERE recipe.recipe_id IN ('%s')" % (id_num))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please type the full recipe name! ')
            show_all_recipe_names()
            continue
        else:
            break
    print(tabulate(result, headers=['ID', 'Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE recipe.recipe_id in ('%s')" % (id_num))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    while True:
        try:
            step_num = input('Please type a step number to remove: ')
            mycursor.execute("SELECT instruction FROM instructions WHERE instruction_num in ('%s') AND recipe_id in ('%s')" % (step_num, id_num))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please choose a valid step! ')
            continue
        else:
            break
    mycursor.execute("DELETE FROM instructions WHERE instruction_num='%s' AND recipe_id='%s'" % (step_num, id_num))
    db.commit()

    menu.display_main_menu()
    menu.main_menu_input()
