import pytest
from Ingredient import Ingredient
from Recipe import Recipe
from ShoppingList import ShoppingList

class TestShoppingList:
    def make_pizza(self):
        recipe = Recipe("Пицца")
        recipe.add_ingredient(Ingredient("Мука", 500, "г"))
        recipe.add_ingredient(Ingredient("Томаты", 200, "г"))
        return recipe
    
    def make_pasta(self):
        recipe = Recipe("Паста")
        recipe.add_ingredient(Ingredient("Мука", 300, "г"))
        recipe.add_ingredient(Ingredient("Яйца", 2, "шт"))
        return recipe
    
    def test_add_recipe_adds_ingredients(self):
        sl = ShoppingList()
        sl.add_recipe(self.make_pizza(), 1)
        assert len(sl._items) == 2

    def test_add_recipe_portions_zero_raises_error(self):
        sl = ShoppingList()
        with pytest.raises(ValueError):
            sl.add_recipe(self.make_pizza(), 0)

    def test_add_recipe_portions_negative_raises_error(self):
        sl = ShoppingList()
        with pytest.raises(ValueError):
            sl.add_recipe(self.make_pizza(), -1)

    def test_add_recipe_scales_portions(self):
        sl = ShoppingList()
        sl.add_recipe(self.make_pizza(), 2)
        # Мука 500 * 2 = 1000
        result = sl.get_list()
        flour = next(i for i in result if i.name == "Мука")
        assert flour.quantity == 1000.0

    def test_remove_recipe_removes_ingredients(self):
        sl = ShoppingList()
        sl.add_recipe(self.make_pizza(), 1)
        sl.remove_recipe("Пицца")
        assert len(sl._items) == 0

    def test_remove_recipe_not_found_no_error(self):
        sl = ShoppingList()
        sl.add_recipe(self.make_pizza(), 1)
        sl.remove_recipe("Борщ")
        assert len(sl._items) == 2

    def test_remove_recipe_removes_only_target(self):
        sl = ShoppingList()
        sl.add_recipe(self.make_pizza(), 1)
        sl.add_recipe(self.make_pasta(), 1)
        sl.remove_recipe("Пицца")
        titles = [t for _, t in sl._items]
        assert "Пицца" not in titles
        assert "Паста" in titles

    def test_get_list_sums_same_ingredients(self):
        sl = ShoppingList()
        sl.add_recipe(self.make_pizza(), 1) 
        sl.add_recipe(self.make_pasta(), 1)
        result = sl.get_list()
        flour = next(i for i in result if i.name == "Мука")
        assert flour.quantity == 800.0

    def test_get_list_sorted_by_name(self):
        sl = ShoppingList()
        sl.add_recipe(self.make_pizza(), 1)
        sl.add_recipe(self.make_pasta(), 1)
        result = sl.get_list()
        names = [i.name for i in result]
        assert names == sorted(names)

    def test_add_combines_two_lists(self):
        sl1 = ShoppingList()
        sl1.add_recipe(self.make_pizza(), 1)
        sl2 = ShoppingList()
        sl2.add_recipe(self.make_pasta(), 1)
        sl3 = sl1 + sl2
        assert len(sl3._items) == len(sl1._items) + len(sl2._items)

    def test_add_does_not_change_originals(self):
        sl1 = ShoppingList()
        sl1.add_recipe(self.make_pizza(), 1)
        original_len = len(sl1._items)
        sl2 = ShoppingList()
        sl2.add_recipe(self.make_pasta(), 1)
        _ = sl1 + sl2
        assert len(sl1._items) == original_len