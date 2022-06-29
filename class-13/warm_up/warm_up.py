def addIngredient(ingredient, sandwich=['bread', 'bread']):
    sandwich.insert(1, ingredient)
    return sandwich

mySandwich = ['bread', 'cheese', 'bread']
mySandwich = addIngredient('butter', mySandwich)
print(mySandwich)

anotherSandwich = addIngredient('turkey')
print(anotherSandwich)

aThirdSandwich = addIngredient('pesto')
print(aThirdSandwich)

