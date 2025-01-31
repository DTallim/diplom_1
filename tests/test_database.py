import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    def test_buns_availability(self):
        """Проверка доступности булочек"""
        db = Database()
        buns = db.available_buns()
        assert len(buns) > 0
        for bun in buns:
            assert isinstance(bun, Bun)
            assert bun.get_price() > 0
            assert len(bun.get_name()) > 0

    def test_ingredients_availability(self):
        """Проверка доступности ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) > 0

        sauces = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) > 0
        for sauce in sauces:
            assert isinstance(sauce, Ingredient)
            assert sauce.get_price() > 0
            assert len(sauce.get_name()) > 0

        fillings = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) > 0
        for filling in fillings:
            assert isinstance(filling, Ingredient)
            assert filling.get_price() > 0
            assert len(filling.get_name()) > 0

    def test_specific_bun_availability(self):
        """Проверка наличия конкретных булочек"""
        db = Database()
        buns = db.available_buns()
        bun_names = [bun.get_name() for bun in buns]
        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names

    def test_specific_ingredients_availability(self):
        """Проверка наличия конкретных ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()
        ingredient_names = [ing.get_name() for ing in ingredients]

        assert "hot sauce" in ingredient_names
        assert "sour cream" in ingredient_names
        assert "chili sauce" in ingredient_names
        assert "cutlet" in ingredient_names
        assert "dinosaur" in ingredient_names
        assert "sausage" in ingredient_names

    def test_ingredients_by_type(self):
        """Проверка количества ингредиентов каждого типа"""
        db = Database()
        ingredients = db.available_ingredients()

        sauces = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        fillings = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]

        assert len(sauces) == 3
        assert len(fillings) == 3