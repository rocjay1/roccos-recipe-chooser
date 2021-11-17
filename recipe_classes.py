class Recipe:

    def __init__(self, name='', ingredients=set(), styles=set()):
        self.name = name
        self.ingredients = ingredients
        self.styles = styles

    def add_ingredients(self, ingredients=set()):
        self.ingredients = self.ingredients.union(ingredients)

    def add_styles(self, styles=set()):
        self.styles = self.styles.union(styles)

    def delete_ingredients(self, ingredients=set()):
        self.ingredients = self.ingredients.difference(ingredients)

    def delete_styles(self, styles=set()):
        self.styles = self.styles.difference(styles)

    def rename(self, name):
        self.name = name
    
    def rename_ingredient(self, ingredient, new_name):
        self.ingredients.remove(ingredient)
        self.ingredients.add(new_name)

    def rename_style(self, style, new_name):
        self.styles.remove(style)
        self.styles.add(new_name)

    def repr_JSON(self):
        return {'__recipe__': True, 'name': self.name, 'ingredients': list(self.ingredients), 'styles': list(self.styles)}

class RecipeBook:

    def __init__(self, name, recipes=dict()):
        self.name = name 
        self.recipes = recipes

    def add_recipe(self, name, ingredients, styles):
        new_recipe = Recipe(name, ingredients, styles)
        self.recipes[name] = new_recipe
        return self.recipes[name]

    def delete_recipe(self, recipe):
        if recipe in self.recipes:
            self.recipes.pop(recipe)
            return self.recipes

    def rename_recipe(self, recipe, new_name):
        if recipe in self.recipes:
            self.recipes[recipe].rename(new_name)
            self.recipes[new_name] = self.recipes[recipe]
            self.recipes.pop(recipe)
            return self.recipes[new_name]
    
    def rename_recipe_ingredient(self, recipe, ingredient, new_name):
        if recipe in self.recipes:
            if ingredient in self.recipes[recipe].ingredients:
                self.recipes[recipe].rename_ingredient(ingredient, new_name)
                return self.recipes[recipe]

    def rename_recipe_style(self, recipe, style, new_name):
        if recipe in self.recipes:
            if style in self.recipes[recipe].styles:
                self.recipes[recipe].rename_style(style, new_name)
                return self.recipes[recipe]

    def add_recipe_ingredients(self, recipe, ingredients):
        if recipe in self.recipes:
            self.recipes[recipe].add_ingredients(set(ingredients))
            return self.recipes[recipe]
    
    def delete_recipe_ingredients(self, recipe, ingredients):
        ingredients = set(ingredients)
        if recipe in self.recipes:
            if self.recipes[recipe].ingredients != self.recipes[recipe].ingredients.difference(ingredients):
                self.recipes[recipe].delete_ingredients(ingredients)
                return self.recipes[recipe]

    def add_recipe_styles(self, recipe, styles):
        if recipe in self.recipes:
            self.recipes[recipe].add_styles(set(styles))
            return self.recipes[recipe]
    
    def delete_recipe_styles(self, recipe, styles):
        styles = set(styles)
        if recipe in self.recipes:
            if self.recipes[recipe].styles != self.recipes[recipe].styles.difference(styles):
                self.recipes[recipe].delete_styles(styles)
                return self.recipes[recipe]

    def list_recipes_by_ingredients(self, ingredients):
        recipes = {}
        for recipe in self.recipes:
            ingred_matches = []
            for ingredient in ingredients:
                if ingredient in self.recipes[recipe].ingredients:
                    ingred_matches.append(ingredient)
            if len(ingred_matches) > 0:
                recipes[recipe] = ingred_matches
        recipes = {r: l for r, l in sorted(recipes.items(), key=lambda item: len(item[1]), reverse=True)}
        if len(recipes) > 0:
            return recipes
        
    def list_recipes_by_styles(self, styles):
        recipes = {}
        for recipe in self.recipes:
            style_matches = []
            for style in styles:
                if style in self.recipes[recipe].styles:
                    style_matches.append(style)
            if len(style_matches) > 0:
                recipes[recipe] = style_matches
        recipes = {r: l for r, l in sorted(recipes.items(), key=lambda item: len(item[1]), reverse=True)}
        if len(recipes) > 0:
            return recipes

    def check_ingredients(self, ingredients):
        all_ings = list()
        for recipe in self.recipes:
            all_ings += self.recipes[recipe].ingredients
        missing_ings = list(set(ingredients).difference(set(all_ings)))
        if len(missing_ings) > 0: 
            return missing_ings

    def check_styles(self, styles):
        all_styles = list()
        for recipe in self.recipes:
            all_styles += self.recipes[recipe].styles
        missing_styles = list(set(styles).difference(set(all_styles)))
        if len(missing_styles) > 0:
            return missing_styles

    def list_recipes(self):
        recipes = ""
        for recipe in self.recipes:
            recipes += f'{self.recipes[recipe].name}, {self.recipes[recipe].ingredients}, {self.recipes[recipe].styles}\n'
        if recipes != "":
            return recipes

    def list_ingredients(self):
        all_ings = list()
        for recipe in self.recipes:
            all_ings += self.recipes[recipe].ingredients
        if len(all_ings) > 0:
            return set(all_ings)

    def list_styles(self):
        all_styles = list()
        for recipe in self.recipes:
            all_styles += self.recipes[recipe].styles
        if len(all_styles) > 0:
            return set(all_styles)

    def repr_JSON(self):
        return {'__recipe_book__': True, 'name': self.name, 'recipes': self.recipes}

if __name__ == '__main__': pass