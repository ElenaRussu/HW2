import pytest
from Ingredient import Ingredient
from Recipe import Recipe

class TestRecipe:
    def test_init_title(self):
        recipe = Recipe("Пицца Маргарита")
        assert recipe.title == "Пицца Маргарита"

    def test_init_ingredients_empty(self):
        recipe = Recipe("Пицца Маргарита")
        assert recipe.ingredients == []

    def test_add_ingredient_new(self):
        recipe = Recipe("Пицца Маргарита")
        ing = Ingredient("Мука", 500, "г")
        recipe.add_ingredient(ing)
        assert len(recipe.ingredients) == 1

    def test_add_ingredient_duplicate_sums_quantity(self):
        recipe = Recipe("Пицца Маргарита")
        recipe.add_ingredient(Ingredient("Мука", 500, "г"))
        recipe.add_ingredient(Ingredient("Мука", 100, "г"))
        assert len(recipe.ingredients) == 1
        assert recipe.ingredients[0].quantity == 600.0

    def test_add_ingredient_different_ingredients(self):
        recipe = Recipe("Пицца Маргарита")
        recipe.add_ingredient(Ingredient("Мука", 500, "г"))
        recipe.add_ingredient(Ingredient("Томаты", 200, "г"))
        assert len(recipe.ingredients) == 2

    def test_scale_returns_new_recipe(self):
        recipe = Recipe("Пицца Маргарита")
        recipe.add_ingredient(Ingredient("Мука", 500, "г"))
        scaled = recipe.scale(2)
        assert scaled is not recipe

    def test_scale_original_not_changed(self):
        recipe = Recipe("Пицца Маргарита")
        recipe.add_ingredient(Ingredient("Мука", 500, "г"))
        recipe.scale(2)
        assert recipe.ingredients[0].quantity == 500.0

    def test_scale_multiplies_quantity(self):
        recipe = Recipe("Пицца Маргарита")
        recipe.add_ingredient(Ingredient("Мука", 500, "г"))
        scaled = recipe.scale(2)
        assert scaled.ingredients[0].quantity == 1000.0

    def test_scale_negative_ratio_raises_error(self):
        recipe = Recipe("Пицца Маргарита")
        with pytest.raises(ValueError):
            recipe.scale(-1)

    def test_scale_zero_ratio_raises_error(self):
        recipe = Recipe("Пицца Маргарита")
        with pytest.raises(ValueError):
            recipe.scale(0)

    def test_len_empty(self):
        recipe = Recipe("Пицца Маргарита")
        assert len(recipe) == 0

    def test_len_with_ingredients(self):
        recipe = Recipe("Пицца Маргарита")
        recipe.add_ingredient(Ingredient("Мука", 500, "г"))
        recipe.add_ingredient(Ingredient("Томаты", 200, "г"))
        assert len(recipe) == 2