import json
from recipe_classes import *

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