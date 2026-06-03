from Ingredient import Ingredient

class Recipe:

    def __init__(self, title: str, ingredients: list = None):
        self.title = title
        self.ingredients = ingredients if ingredients is not None else []

    def add_ingredient(self, ingredient):
        for existing in self.ingredients:
            if existing == ingredient:
                existing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        return isinstance(ratio, (int, float)) and ratio > 0

    def scale(self, ratio: float):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным числом")
        scaled_ingredients = [
            Ingredient(ing.name, ing.quantity * ratio, ing.unit)
            for ing in self.ingredients
        ]
        return Recipe(self.title, scaled_ingredients)

    def __len__(self) -> int:
        return len(self.ingredients)

    def __str__(self) -> str:
        ingredients_str = "\n".join(
            f"  - {ing}" for ing in self.ingredients
        )
        return f"Рецепт: {self.title}\nИнгредиенты:\n{ingredients_str}"