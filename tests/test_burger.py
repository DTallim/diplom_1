import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from helpers import (
    validate_price,
    validate_name,
    create_test_burger,
    format_receipt,
    calculate_burger_price
)
from data import bun_data, ingredients


def get_ingredient_type(type_str):
    """Преобразует строковый тип ингредиента в константу из модуля"""
    return INGREDIENT_TYPE_SAUCE if type_str == 'SAUCE' else INGREDIENT_TYPE_FILLING



@pytest.fixture
def test_bun():
    return Bun(name=bun_data[0], price=float(bun_data[1]))


@pytest.fixture
def test_filling():
    return Ingredient(
        ingredient_type=INGREDIENT_TYPE_FILLING,
        name=ingredients[1][1],
        price=float(ingredients[1][2])
    )


@pytest.fixture
def test_sauce():
    return Ingredient(
        ingredient_type=INGREDIENT_TYPE_SAUCE,
        name=ingredients[4][1],
        price=float(ingredients[4][2])
    )


@pytest.fixture
def empty_burger():
    return Burger()


class TestBurger:
    def test_buns(self, empty_burger, test_bun):
        """Тестирует установку булочек в бургер"""
        empty_burger.set_buns(test_bun)
        assert empty_burger.bun == test_bun
        assert validate_name(empty_burger.bun.get_name())
        assert validate_price(empty_burger.bun.get_price())

    def test_add_ingredient(self, empty_burger, test_filling):
        """Тестирует добавление ингредиента в бургер"""
        empty_burger.add_ingredient(test_filling)
        assert test_filling in empty_burger.ingredients
        assert validate_name(test_filling.get_name())
        assert validate_price(test_filling.get_price())

    def test_remove_ingredient(self, empty_burger, test_filling):
        """Тестирует удаление ингредиента из бургера"""
        empty_burger.add_ingredient(test_filling)
        ingredient_index = empty_burger.ingredients.index(test_filling)
        empty_burger.remove_ingredient(ingredient_index)
        assert test_filling not in empty_burger.ingredients

    def test_move_ingredient(self, empty_burger, test_filling, test_sauce):
        """Тестирует перемещение ингредиентов в бургере"""
        empty_burger.add_ingredient(test_filling)
        empty_burger.add_ingredient(test_sauce)

        original_index = empty_burger.ingredients.index(test_filling)
        new_index = original_index + 1
        empty_burger.move_ingredient(original_index, new_index)

        assert empty_burger.ingredients.index(test_filling) == new_index

    def test_get_price(self, test_bun, test_filling, test_sauce):
        """Тестирует расчет общей стоимости бургера"""
        ingredients_list = [test_filling, test_sauce]
        burger = create_test_burger(test_bun, ingredients_list)

        expected_price = calculate_burger_price(test_bun, ingredients_list)
        actual_price = burger.get_price()

        assert actual_price == expected_price
        assert validate_price(actual_price)

    def test_get_receipt(self, test_bun, test_filling, test_sauce):
        """Тестирует формирование чека бургера"""
        ingredients_list = [test_filling, test_sauce]
        burger = create_test_burger(test_bun, ingredients_list)

        expected_receipt = format_receipt(
            test_bun.get_name(),
            ingredients_list,
            burger.get_price()
        )

        actual_receipt = burger.get_receipt()
        assert expected_receipt in actual_receipt

    @pytest.mark.parametrize("ingredient_data", [
        [],  # пустой список ингредиентов
        [ingredients[2]],  # один ингредиент
        [ingredients[3], ingredients[5]]  # несколько ингредиентов
    ])
    def test_burger_with_different_ingredients(self, test_bun, ingredient_data):
        """Тестирует создание бургера с разным количеством ингредиентов"""
        ingredients_list = [
            Ingredient(
                ingredient_type=get_ingredient_type(ing_data[0]),
                name=ing_data[1],
                price=float(ing_data[2])
            )
            for ing_data in ingredient_data
        ] if ingredient_data else []

        burger = create_test_burger(test_bun, ingredients_list)

        assert burger.bun == test_bun
        assert len(burger.ingredients) == len(ingredients_list)
        assert burger.get_price() == calculate_burger_price(test_bun, ingredients_list)
