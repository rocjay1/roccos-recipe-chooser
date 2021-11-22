import json

class Recipe:

    def __init__(self, name='', ingredients=set(), styles=set()):
        self.name = name
        self.ingredients = ingredients
        self.styles = styles

    def rename(self, name):
        self.name = name

    def repr_JSON(self):
        return {'__recipe__': True, 'name': self.name, 
            'ingredients': list(self.ingredients), 'styles': list(self.styles)}

class RecipeBook:

    def __init__(self, name='main', recipes=dict()):
        self.name = name 
        self.recipes = recipes

    def check_recipe(self, recipe):
        if recipe in self.recipes:
            return True

    def add_recipe(self, name, ingredients, styles):
        if self.check_recipe(name):
            return 
        new_recipe = Recipe(name, set(ingredients), set(styles))
        self.recipes[name] = new_recipe

    def delete_recipe(self, recipe):
        if self.check_recipe(recipe):
            self.recipes.pop(recipe)

    def update_recipe(self, old_name, new_name, ingredients, styles):
        if self.check_recipe(new_name):
            pass
        else:
            self.recipes[old_name].rename(new_name)
            self.recipes[new_name] = self.recipes[old_name]
            self.recipes.pop(old_name)
        self.recipes[new_name].ingredients = set(ingredients)
        self.recipes[new_name].styles = set(styles)

    def get_recipes_by_attr(self, attr, names):
        if attr not in ['ing', 'sty']:
            return
        recipes = {}
        for recipe in self.recipes:
            matches = []
            for name in names:
                if attr == 'ing':
                    if name in self.recipes[recipe].ingredients:
                        matches.append(name)
                else:
                    if name in self.recipes[recipe].styles:
                        matches.append(name)
            if len(matches) > 0:
                recipes[recipe] = matches
        recipes = {r: l for r, l in sorted(recipes.items(), 
            key=lambda item: len(item[1]), reverse=True)}
        return recipes

    def repr_JSON(self):
        return {'__recipe_book__': True, 'name': self.name, 'recipes': self.recipes}

class RecipeEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'repr_JSON'):
            return obj.repr_JSON()
        else:
            return json.JSONEncoder.default(self, obj)

def recipe_decoder(dct):
    if '__recipe__' in dct:
        return Recipe(dct['name'], set(dct["ingredients"]), set(dct["styles"]))
    elif '__recipe_book__' in dct:
        return RecipeBook(dct['name'], dct['recipes'])
    else:
        return dct

def write_JSON(content, file_path):
    with open(file_path, "w") as data_file:
        json.dump(content, data_file, cls=RecipeEncoder)

def read_JSON(file_path):
    with open(file_path) as data_file:
        data = data_file.read()   
        data_object = json.loads(data, object_hook=recipe_decoder)
    return data_object

if __name__ == '__main__': pass