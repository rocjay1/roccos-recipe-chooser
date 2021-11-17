class _Recipe:

    def __init__(self, name='', ingredients=set(), styles=set()):
        self.name = name
        self.ingredients = ingredients
        self.styles = styles

    def add_ingredients(self, ingredients):
        self.ingredients = self.ingredients.union(ingredients)

    def add_styles(self, styles):
        self.styles = self.styles.union(styles)

    def delete_ingredients(self, ingredients):
        self.ingredients = self.ingredients.difference(ingredients)

    def delete_styles(self, styles):
        self.styles = self.styles.difference(styles)

    def rename(self, name):
        self.name = name
    
    def rename_ingredient(self, old_name, new_name):
        if old_name in self.ingredients:
            self.ingredients.remove(old_name)
            self.ingredients.add(new_name)

    def rename_style(self, old_name, new_name):
        if old_name in self.styles:
            self.styles.remove(old_name)
            self.styles.add(new_name)

    def repr_JSON(self):
        return {'__recipe__': True, 'name': self.name, 'ingredients': list(self.ingredients), 'styles': list(self.styles)}

class RecipeBook:

    def __init__(self, name, recipes=dict()):
        self.name = name 
        self.recipes = recipes

    def add_recipe(self, name, ingredients, styles):
        new_recipe = _Recipe(name, ingredients, styles)
        self.recipes[name] = new_recipe

    def delete_recipe(self, recipe):
        if recipe in self.recipes:
            self.recipes.pop(recipe)

    def rename_recipe(self, recipe, new_name):
        if recipe in self.recipes:
            self.recipes[recipe].rename(new_name)
            self.recipes[new_name] = self.recipes[recipe]
            self.recipes.pop(recipe)
    
    def rename_recipe_ingredient(self, recipe, ingredient, new_name):
        if recipe in self.recipes:
            self.recipes[recipe].rename_ingredient(ingredient, new_name)

    def rename_recipe_style(self, recipe, style, new_name):
        if recipe in self.recipes:
            self.recipes[recipe].rename_style(style, new_name)

    def add_recipe_ingredients(self, recipe, ingredients):
        if recipe in self.recipes:
            self.recipes[recipe].add_ingredients(set(ingredients))
    
    def delete_recipe_ingredients(self, recipe, ingredients):
        if recipe in self.recipes:
            self.recipes[recipe].delete_ingredients(set(ingredients))

    def add_recipe_styles(self, recipe, styles):
        if recipe in self.recipes:
            self.recipes[recipe].add_styles(set(styles))
    
    def delete_recipe_styles(self, recipe, styles):
        if recipe in self.recipes:
            self.recipes[recipe].delete_styles(set(styles))

    def get_recipes_by_ingredients(self, ingredients):
        recipes = {}
        for recipe in self.recipes:
            matches = []
            for ingredient in ingredients:
                if ingredient in self.recipes[recipe].ingredients:
                    matches.append(ingredient)
            if len(matches) > 0:
                recipes[recipe] = matches
        recipes = {r: l for r, l in sorted(recipes.items(), key=lambda item: len(item[1]), reverse=True)}
        return recipes
        
    def get_recipes_by_styles(self, styles):
        recipes = {}
        for recipe in self.recipes:
            matches = []
            for style in styles:
                if style in self.recipes[recipe].styles:
                    matches.append(style)
            if len(matches) > 0:
                recipes[recipe] = matches
        recipes = {r: l for r, l in sorted(recipes.items(), key=lambda item: len(item[1]), reverse=True)}
        if len(recipes) > 0:
            return recipes

    # def check_ingredients(self, ingredients):
    #     all_ings = list()
    #     for recipe in self.recipes:
    #         all_ings += self.recipes[recipe].ingredients
    #     missing_ings = list(set(ingredients).difference(set(all_ings)))
    #     if len(missing_ings) > 0: 
    #         return missing_ings

    # def check_styles(self, styles):
    #     all_styles = list()
    #     for recipe in self.recipes:
    #         all_styles += self.recipes[recipe].styles
    #     missing_styles = list(set(styles).difference(set(all_styles)))
    #     if len(missing_styles) > 0:
    #         return missing_styles

    # def list_recipes(self):
    #     recipes = ""
    #     for recipe in self.recipes:
    #         recipes += f'{self.recipes[recipe].name}, {self.recipes[recipe].ingredients}, {self.recipes[recipe].styles}\n'
    #     if recipes != "":
    #         return recipes

    # def list_ingredients(self):
    #     all_ings = list()
    #     for recipe in self.recipes:
    #         all_ings += self.recipes[recipe].ingredients
    #     if len(all_ings) > 0:
    #         return set(all_ings)

    # def list_styles(self):
    #     all_styles = list()
    #     for recipe in self.recipes:
    #         all_styles += self.recipes[recipe].styles
    #     if len(all_styles) > 0:
    #         return set(all_styles)

    def repr_JSON(self):
        return {'__recipe_book__': True, 'name': self.name, 'recipes': self.recipes}

if __name__ == '__main__': pass