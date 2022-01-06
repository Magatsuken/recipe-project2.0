class Recipe:
    def __init__(self, name, cook_time, method, ingredients, preparation, quantity, instructions):
        self.name = name
        self.cook_time = cook_time
        self.method = method
        self.ingredients = ingredients
        self.preparation = preparation
        self.quantity = quantity
        self.instructions = instructions


    def __repr__(self):
        return "Recipe name: %s\nCook Time: %s\nMethod: %s\nIngredients: %s\nInstructions: %s" % (self.name, self.cook_time, self.method, self.ingredients, self.instructions)