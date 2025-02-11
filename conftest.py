import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import bun_data, ingredients


@pytest.fixture
def test_bun():
    return Bun("test bun", 100.0)


@pytest.fixture
def test_filling():
    """Фикстура, создающая тестовый ингредиент-начинку"""
    ing_data = ingredients[1]  # Биокотлета
    return Ingredient(
        ingredient_type=INGREDIENT_TYPE_FILLING,
        name=ing_data[1],
        price=float(ing_data[2])
    )


@pytest.fixture
def test_sauce():
    """Фикстура, создающая тестовый ингредиент-соус"""
    ing_data = ingredients[4]  # Соус фирменный
    return Ingredient(
        ingredient_type=INGREDIENT_TYPE_SAUCE,
        name=ing_data[1],
        price=float(ing_data[2])
    )


@pytest.fixture
def empty_burger():
    """Фикстура, создающая пустой бургер"""
    return Burger()