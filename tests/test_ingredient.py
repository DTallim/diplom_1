import pytest
from conftest import test_sauce,test_filling
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    def test_sauce_properties(self, test_sauce):
        """Проверка свойств соуса"""
        assert test_sauce.get_type() == INGREDIENT_TYPE_SAUCE
        assert test_sauce.get_price() == 50.0
        assert test_sauce.get_name() == "test sauce"

    def test_filling_properties(self, test_filling):
        """Проверка свойств начинки"""
        assert test_filling.get_type() == INGREDIENT_TYPE_FILLING
        assert test_filling.get_price() == 150.0
        assert test_filling.get_name() == "test filling"

    def test_ingredient_str_representation(self, test_sauce):
        """Проверка строкового представления ингредиента"""
        assert str(test_sauce)
        assert isinstance(str(test_sauce), str)