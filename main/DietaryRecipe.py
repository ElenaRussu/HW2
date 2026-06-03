from Ingredient import Ingredient
from Recipe import Recipe

class DietaryRecipe(Recipe):
     def __init__(self, title: str, diet_type: str, ingredients: list = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

     def scale(self, ratio: float):
         if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным числом")
         scaled = super().scale(ratio)
         return DietaryRecipe(scaled.title, self.diet_type, scaled.ingredients)

     def __str__(self) -> str:
            parent_str = super().__str__()
            return f"[{self.diet_type}] {parent_str}"