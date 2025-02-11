import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from helpers import (
    validate_buns,
    validate_ingredients_by_type,
    get_ingredient_names,
    get_bun_names,
    count_ingredients_by_type
)


class TestDatabase:
    def test_buns_availability(self):
        """Проверка доступности булочек"""
        db = Database()
        buns = db.available_buns()
        assert validate_buns(buns)

    def test_ingredients_availability(self):
        """Проверка доступности ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) > 0

        assert validate_ingredients_by_type(ingredients, INGREDIENT_TYPE_SAUCE)
        assert validate_ingredients_by_type(ingredients, INGREDIENT_TYPE_FILLING)

    def test_specific_bun_availability(self):
        """Проверка наличия конкретных булочек"""
        db = Database()
        buns = db.available_buns()
        bun_names = get_bun_names(buns)

        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names

    def test_specific_ingredients_availability(self):
        """Проверка наличия конкретных ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()
        ingredient_names = get_ingredient_names(ingredients)

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

        assert count_ingredients_by_type(ingredients, INGREDIENT_TYPE_SAUCE) == 3
        assert count_ingredients_by_type(ingredients, INGREDIENT_TYPE_FILLING) == 3