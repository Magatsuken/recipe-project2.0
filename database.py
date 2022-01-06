from tabulate import tabulate
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='recipedb'
)

mycursor = db.cursor()
'''
Creates a database
'''
# mycursor.execute('CREATE DATABASE recipedb')
'''
Creates a table
'''


# mycursor.execute('CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)')
# mycursor.execute('DESCRIBE Person')
# mycursor.execute('INSERT INTO Person (name, age) VALUES (%s,%s)', ('Joe', 22))

# for x in mycursor:
#    print(x)


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