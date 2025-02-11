import pytest
from conftest import test_sauce, test_filling
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    def test_sauce_type(self, test_sauce):
        """Проверка типа соуса"""
        assert test_sauce.get_type() == INGREDIENT_TYPE_SAUCE

    def test_sauce_price(self, test_sauce):
        """Проверка цены соуса"""
        assert test_sauce.get_price() == 15.0

    def test_sauce_name(self, test_sauce):
        """Проверка названия соуса"""
        assert test_sauce.get_name() == "Соус традиционный галактический"

    def test_filling_type(self, test_filling):
        """Проверка типа начинки"""
        assert test_filling.get_type() == INGREDIENT_TYPE_FILLING

    def test_filling_price(self, test_filling):
        """Проверка цены начинки"""
        assert test_filling.get_price() == 424.0

    def test_filling_name(self, test_filling):
        """Проверка названия начинки"""
        assert test_filling.get_name() == "Биокотлета из марсианский Магнолии"

    def test_ingredient_has_str_representation(self, test_sauce):
        """Проверка наличия строкового представления ингредиента"""
        assert str(test_sauce)

    def test_ingredient_str_returns_string(self, test_sauce):
        """Проверка типа возвращаемого значения str()"""
        assert isinstance(str(test_sauce), str)