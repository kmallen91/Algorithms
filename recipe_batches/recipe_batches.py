#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    max = 1000
    for item in recipe:
        if item in ingredients:
            if (ingredients[f'{item}'] // recipe[f'{item}']) < max:
                max = (ingredients[f'{item}'] // recipe[f'{item}'])
        else:
            return 0
    return max


ex_recipe = {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}
ex_ingredients = {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}
print(recipe_batches(ex_recipe, ex_ingredients))

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
