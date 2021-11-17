from os import name
from read_write import *

# Helper functions for formatting
def format_to_list(str):
    lst = str.split(",") 
    lst = list(map(lambda s: s.lower().strip(), lst))
    return lst

def format_to_str(str):
    return str.lower().strip()

# Global input vars
ent = "Press ENTER to continue "
val = "\nPlease enter a valid option.\n"
ing_q = "\nWhat are the ingredients? "
sty_q = "\nWhat are the styles? "
name_q = "\nWhat is the name of the recipe? "
new_name_q = "\nWhat is the new name? "
no_ex = "\nThe recipe does not exist or the recipe does not contain that attribute.\n"

try:
    # Read in JSON data as RecipeBook object
    data = read_JSON("recipes.json")
except:
    data = RecipeBook()
    
print("\n===========Welcome to the Recipe Book (v1)===========\n")
s = ("Some things to remember...\n"
"* Be careful with entering information, the app is\n"
"still very sensitive to misspellings")
print(s)

while True:
    s = ("\n[1] List recipes, ingredients, or styles\n"
    "[2] Get recipes by ingredients\n"
    "[3] Get recipes by styles\n"
    "[4] Add/delete a recipe\n"
    "[5] Add/delete ingredients to/from a recipe\n"
    "[6] Add/delete styles to/from a recipe\n"
    "[7] Rename a recipe or one of its styles/ingredients\n"
    "[8] Save\n"
    "[9] Exit")
    print(s) # Main menu
    init_input = input("\nWhat would you like to do? ")

    if init_input == '1':
        while True:
            dec_input = input("\nWould you like to [1] list recipes [2] list ingredients [3] list styles [4] go back? ")
            if dec_input == '1':
                output = data.list_recipes()
                if output:
                    print(f"\nThe recipes are:\n\n{output}")
                else:
                    print("\nThere are no recipes.\n")
                # Wait for key press
                next_input = input(ent)
                if next_input == '':
                    break
            elif dec_input == '2':
                output = data.list_ingredients()
                if output:
                    print(f'\nThe ingredients are:\n\n{output}.\n')
                else:
                    print("\nThere are no ingredients.\n")
                next_input = input(ent)
                if next_input == '':
                    break
            elif dec_input ==  '3':
                output = data.list_styles()
                if output:
                    print(f'\nThe styles are:\n\n{output}.\n')
                else:
                    print("\nThere are no styles.\n")
                next_input = input(ent)
                if next_input == '':
                    break
            elif dec_input == '4':
                break
            else:
                print(val)
                next_input = input(ent)
                if next_input == '':
                    continue

    elif init_input == '2':
        ing_input = input(ing_q) 
        ing_input = format_to_list(ing_input) 
        check_output = data.check_ingredients(ing_input) # check for missing ingredients
        if check_output:
            print(f'\nThe following ingredients are not in the book: {check_output}.')
        list_output = data.list_recipes_by_ingredients(ing_input)
        if list_output:
            s = "\n"
            for item in list_output.items(): 
                s += f"{item[0]} has ingredients: {item[1]}.\n"
            print(s)
        else:
            print("\nThere are no matches.\n")
        next_input = input(ent)
        if next_input == '':
            continue

    elif init_input == '3':
        sty_input = input(sty_q)
        sty_input = format_to_list(sty_input)
        check_output = data.check_styles(sty_input)
        if check_output:
            print(f'\nThe following styles are not in the book: {check_output}.')
        list_output = data.list_recipes_by_styles(sty_input)
        if list_output:
            s = "\n"
            for item in list_output.items(): 
                s += f"{item[0]} has styles: {item[1]}.\n"
            print(s)
        else:
            print("\nThere are no matches.\n")
        next_input = input(ent)
        if next_input == '':
            continue

    elif init_input == '4':
        while True:
            dec_input = input("\nWould you like to [1] add a recipe [2] delete a recipe [3] go back? ")

            if dec_input == '1':
                name_input = input(name_q)
                name_input = format_to_str(name_input)
                ing_input = input(ing_q)
                ing_input = format_to_list(ing_input)
                sty_input = input(sty_q)
                sty_input = format_to_list(sty_input)
                output = data.add_recipe(name_input, ing_input, sty_input)
                if output:
                    print(f"\nYou have added recipe {output.name} with ingredients: {output.ingredients} and styles: {output.styles}.\n")
                    next_input = input(ent)
                    if next_input == '':
                        break
                else:
                    print("\nThere was an error.\n")
            
            elif dec_input == '2':
                name_input = input(name_q)
                name_input = format_to_str(name_input)
                output = data.delete_recipe(name_input) 
                if output:
                    print(f"\nYou have deleted recipe {name_input}.\n")
                    next_input = input(ent)
                    if next_input == '':
                        break
                else:
                    print(no_ex)
                    next_input = input(ent)
                    if next_input == '':
                        continue

            elif dec_input == '3':
                break
            
            else:
                print(val)
                next_input = input(ent)
                if next_input == '':
                    continue
    
    elif init_input == '5':
        while True:
            dec_input = input("\nWould you like to [1] add an ingredient to a recipe [2] delete an ingredient from a recipe [3] go back? ")

            if dec_input == '1':
                name_input = input(name_q)
                name_input = format_to_str(name_input)
                ing_input = input(ing_q)
                ing_input = format_to_list(ing_input)
                output = data.add_recipe_ingredients(name_input, ing_input)
                if output:
                    print(f"\nIngredients: {ing_input} have been added.\n")
                    next_input = input(ent)
                    if next_input == '':
                        break
                else:
                    print(no_ex)
                    next_input = input(ent)
                    if next_input == '':
                        continue
            
            elif dec_input == '2':
                name_input = input(name_q)
                name_input = format_to_str(name_input)
                ing_input = input(ing_q)
                ing_input = format_to_list(ing_input)
                check_output = data.check_ingredients(ing_input) # check for missing ingredients
                if check_output:
                    print(f'\nThe following ingredients are not in the book: {check_output}.')
                del_output = data.delete_recipe_ingredients(name_input, ing_input)
                if del_output:
                    print(f"\nIngredients: {ing_input} have been deleted.\n")
                    next_input = input(ent)
                    if next_input == '':
                        break
                else:
                    print(no_ex)
                    next_input = input(ent)
                    if next_input == '':
                        continue
            
            elif dec_input == '3':
                break

            else:
                print(val)
                next_input = input(ent)
                if next_input == '':
                    continue
            
    elif init_input == '6':
        while True:
            dec_input = input("\nWould you like to [1] add a style to a recipe [2] delete a style from a recipe [3] go back? ")

            if dec_input == '1':
                name_input = input(name_q)
                name_input = format_to_str(name_input)
                sty_input = input(sty_q)
                sty_input = format_to_list(sty_input)
                output = data.add_recipe_styles(name_input, sty_input)
                if output:
                    print(f"\nStyles: {sty_input} have been added.\n")
                    next_input = input(ent)
                    if next_input == '':
                        break
                else:
                    print(no_ex)
                    next_input = input(ent)
                    if next_input == '':
                        continue
            
            elif dec_input == '2':
                name_input = input(name_q)
                name_input = format_to_str(name_input)
                sty_input = input(sty_q)
                sty_input = format_to_list(sty_input)
                check_output = data.check_styles(sty_input) 
                if check_output:
                    print(f'\nThe following styles are not in the book: {check_output}.')
                del_output = data.delete_recipe_styles(name_input, sty_input)
                if del_output:
                    print(f"\nStyles: {sty_input} have been deleted.\n")
                    next_input = input(ent)
                    if next_input == '':
                        break
                else:
                    print(no_ex)
                    next_input = input(ent)
                    if next_input == '':
                        continue
            
            elif dec_input == '3':
                break

            else:
                print(val)
                next_input = input(ent)
                if next_input == '':
                    continue

    elif init_input == '7':
        while True:
            dec_input = input("\nWould you like to [1] rename a recipe [2] rename a recipe's ingredient [3] rename a recipe's style [4] go back? ")

            if dec_input == '1':
                name_input = input(name_q)
                name_input = format_to_str(name_input)
                new_name_input = input(new_name_q)
                new_name_input = format_to_str(new_name_input)
                output = data.rename_recipe(name_input, new_name_input)
                if output:
                    print(f"\nRecipe {name_input} has been renamed to {new_name_input}.\n")
                    next_input = input(ent)
                    if next_input == '':
                        break
                else:
                    print(no_ex)
                    next_input = input(ent)
                    if next_input == '':
                        continue

            elif dec_input == '2':
                name_input = input(name_q)
                name_input = format_to_str(name_input)
                ing_input = input("\nWhat is the ingredient? ")
                ing_input = format_to_str(ing_input)
                new_name_input = input(new_name_q)
                new_name_input = format_to_str(new_name_input)
                output = data.rename_recipe_ingredient(name_input, ing_input, new_name_input)
                if output:
                    print(f"\nRecipe {name_input}'s ingredient {ing_input} has been renamed to {new_name_input}.\n")
                    next_input = input(ent)
                    if next_input == '':
                        break
                else:
                    print(no_ex)
                    next_input = input(ent)
                    if next_input == '':
                        continue

            elif dec_input == '3':
                name_input = input(name_q)
                name_input = format_to_str(name_input)
                sty_input = input("\nWhat is the style? ")
                sty_input = format_to_str(sty_input)
                new_name_input = input(new_name_q)
                new_name_input = format_to_str(new_name_input)
                output = data.rename_recipe_style(name_input, sty_input, new_name_input)
                if output:
                    print(f"\nRecipe {name_input}'s style {sty_input} has been renamed to {new_name_input}.\n")
                    next_input = input(ent)
                    if next_input == '':
                        break
                else:
                    print(no_ex)
                    next_input = input(ent)
                    if next_input == '':
                        continue

            elif dec_input == '4':
                break

            else:
                print(val)
                next_input = input(ent)
                if next_input == '':
                    continue

    elif init_input == '8':
        try:
            write_JSON(data, "recipes.json")
            print("\nData saved.\n")
            next_input = input(ent)
            if next_input == '':
                continue
        except Exception as e:
            print("\n" + e + "\n")

    elif init_input == '9':
        print()
        break

    else:
        print(val)
        next_input = input(ent)
        if next_input == '':
            continue