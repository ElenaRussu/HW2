from Ingredient import Ingredient
from Recipe import Recipe

class ShoppingList:
    def __init__(self):
        self._items = []

def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)
        for ingredient in scaled.ingredients:
            self._items.append((ingredient, recipe.title))

def remove_recipe(self, title: str):
        self._items = [
            (ing, t) for (ing, t) in self._items
            if t != title
        ]
def get_list(self) -> list:
        totals = {}
        for ingredient, _ in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in totals:
                totals[key] += ingredient.quantity
            else:
                totals[key] = ingredient.quantity
        result = [
            Ingredient(name, quantity, unit)
            for (name, unit), quantity in totals.items()
        ]
        return sorted(result, key=lambda ing: ing.name)

def __add__(self, other):
    new_list = ShoppingList()
    new_list._items = self._items + other._items
    return new_list