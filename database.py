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
    mycursor.execute('SELECT name FROM recipe')
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Name'], tablefmt='psql'))


def select_recipe():
    while True:
        try:
            user_input = input('Please type a recipe name: ')
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
    print(tabulate(result, headers=['Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE name in ('%s')" % (user_input))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE name in ('%s')" % (user_input))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))


def search_by_name():
    while True:
        try:
            user_input = input('Please type a recipe name: ')
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
    print(tabulate(result, headers=['Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute("SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE name in ('%s')" % (user_input))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute("SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE name in ('%s')" % (user_input))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))


def search_by_ingredient():
    while True:
        try:
            user_input = input('Please type an ingredient: ')
            mycursor.execute("SELECT name, cook_time, method FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE ingredient in ('%s')" % (user_input))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please choose another ingredient! ')
            continue
        else:
            break
    print(tabulate(result, headers=['Name', 'Cook Time', 'Method'], tablefmt='psql'))
    search_by_name()


def search_by_cook_time():
    while True:
        try:
            user_input = float(input('Please type how much time in hours: '))
            if user_input < 0:
                raise ValueError
            mycursor.execute("SELECT name, cook_time, method FROM recipe WHERE cook_time <= ('%s')" % (user_input))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please try another cook time! ')
            continue
        else:
            break
    print(tabulate(result, headers=['Name', 'Cook Time', 'Method'], tablefmt='psql'))
    search_by_name()


def search_by_method():
    while True:
        try:
            user_input = input('Please type a cooking method: ')
            mycursor.execute("SELECT name, cook_time, method FROM recipe WHERE method IN ('%s')" % (user_input))
            result = mycursor.fetchall()
            if result == []:
                raise ValueError
        except ValueError:
            print('Please try another cooking method! ')
            continue
        else:
            break
    print(tabulate(result, headers=['Name', 'Cook Time', 'Method'], tablefmt='psql'))
    search_by_name()


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
            ingredient_prep.append(recipe_prep)
            quantity = input('How many ingredients do you use? IE 6 slices, 2 breasts. ')
            quantity_list.append(quantity)
        step_counter += 1
    ingredient_list.pop()
    ingredient_prep.pop()
    quantity_list.pop()

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

    for ingredient in new_recipe.ingredients:
        for preparation in new_recipe.preparation:
            for quantity in new_recipe.quantity:
                mycursor.execute("SELECT recipe_id FROM recipe ORDER BY recipe_id DESC LIMIT 1")
                result = mycursor.fetchone()
                for x in result:
                    recipe_id = x
                    mycursor.execute("INSERT INTO ingredients(recipe_id, ingredient, preparation, quantity) VALUES ('%s', '%s', '%s', '%s')" % (recipe_id, ingredient, preparation, quantity))

    instruction_num = 1
    for instruction in instruction_list:
        mycursor.execute("SELECT recipe_id FROM recipe ORDER BY recipe_id DESC LIMIT 1")
        result = mycursor.fetchone()
        for x in result:
            recipe_id = x
        mycursor.execute("INSERT INTO instructions(recipe_id, instruction_num, instruction) VALUES ('%s', '%s', '%s')" % (recipe_id, instruction_num, instruction))
        instruction_num += 1

    db.commit()


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


def edit_entry():
    menu.display_edit_menu()
    menu.edit_menu_input()


def edit_name():
    while True:
        try:
            show_all_recipe_names()
            user_input = input('Please type a recipe that you want to edit: ')
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
    print(tabulate(result, headers=['Name', 'Cook Time', 'Method'], tablefmt='psql'))
    mycursor.execute(
        "SELECT ingredient, preparation, quantity FROM recipe INNER JOIN ingredients ON recipe.recipe_id = ingredients.recipe_id WHERE name in ('%s')" % (
            user_input))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Ingredient', 'Preparation', 'Quantity'], tablefmt='psql'))
    mycursor.execute(
        "SELECT instruction_num, instruction FROM recipe INNER JOIN instructions ON recipe.recipe_id = instructions.recipe_id WHERE name in ('%s')" % (
            user_input))
    result = mycursor.fetchall()
    print(tabulate(result, headers=['Step #', 'Instruction'], tablefmt='psql'))

    new_name = input('What do you want the new name to be? ')
    mycursor.execute("UPDATE recipe SET name = '%s' WHERE name IN ('%s')" % (new_name, user_input))
    db.commit()