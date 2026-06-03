import pytest
from Ingredient import Ingredient

class TestIngredient:
    def test_init_name(self):
        ing = Ingredient("Мука", 500, "г")
        assert ing.name == "Мука"

    def test_init_quantity(self):
        ing = Ingredient("Мука", 500, "г")
        assert ing.quantity == 500.0

    def test_init_unit(self):
        ing = Ingredient("Мука", 500, "г")
        assert ing.unit == "г"

    def test_quantity_converts_to_float(self):
        ing = Ingredient("Мука", 500, "г")
        assert isinstance(ing.quantity, float)

    def test_quantity_negative_raises_error(self):
        with pytest.raises(ValueError):
            Ingredient("Мука", -1, "г")

    def test_quantity_zero_raises_error(self):
        with pytest.raises(ValueError):
            Ingredient("Мука", 0, "г")

    def test_str(self):
        ing = Ingredient("Мука", 500, "г")
        assert str(ing) == "Мука: 500.0 г"

    def test_eq_same_name_and_unit_different_quantity(self):
        ing1 = Ingredient("Мука", 500, "г")
        ing2 = Ingredient("Мука", 200, "г")
        assert ing1 == ing2

    def test_eq_different_name(self):
        ing1 = Ingredient("Мука", 500, "г")
        ing2 = Ingredient("Соль", 500, "г")
        assert ing1 != ing2

    def test_eq_different_unit(self):
        ing1 = Ingredient("Мука", 500, "г")
        ing2 = Ingredient("Мука", 500, "кг")
        assert ing1 != ing2
    
