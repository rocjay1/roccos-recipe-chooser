class Recipe:

    def __init__(self, name='', ingredients=set(), styles=set()):
        self.name = name
        self.ingredients = ingredients
        self.styles = styles

    # def add_ingredients(self, ingredients):
    #     self.ingredients = self.ingredients.union(ingredients)

    # def add_styles(self, styles):
    #     self.styles = self.styles.union(styles)

    # def delete_ingredients(self, ingredients):
    #     self.ingredients = self.ingredients.difference(ingredients)

    # def delete_styles(self, styles):
    #     self.styles = self.styles.difference(styles)

    def rename(self, name):
        self.name = name
    
    # def rename_ingredient(self, old_name, new_name):
    #     if self.check_ingredient(old_name):
    #         self.ingredients.remove(old_name)
    #         self.ingredients.add(new_name)

    # def rename_style(self, old_name, new_name):
    #     if self.check_style(old_name):
    #         self.styles.remove(old_name)
    #         self.styles.add(new_name)

    # def check_ingredient(self, ingredient):
    #     if ingredient in self.ingredients:
    #         return True

    # def check_style(self, style):
    #     if style in self.styles:
    #         return True

    def repr_JSON(self):
        return {'__recipe__': True, 'name': self.name, 'ingredients': list(self.ingredients), 'styles': list(self.styles)}

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

    # def rename_recipe(self, old_name, new_name):
    #     if self.check_recipe(old_name):
    #         self.recipes[old_name].rename(new_name)
    #         self.recipes[new_name] = self.recipes[old_name]
    #         self.recipes.pop(old_name)

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
        recipes = {r: l for r, l in sorted(recipes.items(), key=lambda item: len(item[1]), reverse=True)}
        return recipes

    def repr_JSON(self):
        return {'__recipe_book__': True, 'name': self.name, 'recipes': self.recipes}

if __name__ == '__main__': pass