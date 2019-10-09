#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []
  for r in recipe.items():
    for i in ingredients.items():
      if r[0] == i[0]:
        batches.append(i[1]//r[1])

  if len(recipe) != len(batches):
    return 0
  else:
    for i in batches:
      if i == 0:
        return 0
      else:
        batches.sort()
        return batches[0]
  # needed = []
  # on_hand = []
  # batches = []
  # for r in recipe.items():
  #   needed.append(r[0])
  #   for i in ingredients.items():
  #     if r[0] == i[0]:
  #       on_hand.append(r[0])
  #       batches.append(i[1]//r[1])

  # if needed != on_hand:
  #   return 0
  # else:
  #   for i in batches:
  #     if i == 0:
  #       return "No"
  #     else:
  #       batches.sort()
  #       return batches[0]

      


      

  print("needed:", needed)
  print("on_hand:", on_hand)
  print("batches:", batches)
    
  # for k, v in recipe.items():
  #   print(k, v)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))