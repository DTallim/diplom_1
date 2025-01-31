import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def test_bun():
    return Bun("test bun", 100.0)

@pytest.fixture
def test_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 50.0)

@pytest.fixture
def test_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "test filling", 150.0)

@pytest.fixture
def empty_burger():
    return Burger()
