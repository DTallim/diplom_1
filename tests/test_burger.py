import pytest
from helpers import (
    create_test_burger,
    format_receipt,
    create_ingredients_list
)
from conftest import empty_burger,test_bun,test_filling,test_sauce


class TestBurger:
    def test_empty_burger(self, empty_burger):
        """Тестирует создание пустого бургера"""
        # Для пустого бургера не вызываем get_price(), так как булочки нет
        assert empty_burger.bun is None
        assert len(empty_burger.ingredients) == 0

    def test_burger_with_bun(self, test_bun):
        """Тестирует создание бургера только с булочкой"""
        burger = create_test_burger(bun=test_bun)
        assert burger.bun == test_bun
        assert len(burger.ingredients) == 0
        # Цена булочки удваивается по логике класса Burger
        assert burger.get_price() == test_bun.get_price() * 2

    def test_burger_with_one_ingredient(self, test_bun, test_filling):
        """Тестирует создание бургера с одним ингредиентом"""
        ingredients_list = [test_filling]
        burger = create_test_burger(test_bun, ingredients_list)

        assert burger.bun == test_bun
        assert len(burger.ingredients) == 1
        # Цена = удвоенная цена булочки + цена ингредиента
        expected_price = (test_bun.get_price() * 2) + test_filling.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt(self, test_bun, test_filling, test_sauce):
        """Тестирует формирование чека бургера"""
        ingredients_list = [test_filling, test_sauce]
        burger = create_test_burger(test_bun, ingredients_list)

        expected_receipt = format_receipt(
            test_bun.get_name(),
            ingredients_list,
            burger.get_price()  # Эта цена уже будет с удвоенной стоимостью булочки
        )

        actual_receipt = burger.get_receipt()
        assert actual_receipt == expected_receipt

    @pytest.mark.parametrize("ingredient_indices", [
        [],  # пустой список ингредиентов
        [1],  # один ингредиент (биокотлета)
        [1, 4]  # несколько ингредиентов (биокотлета и соус)
    ])
    def test_burger_with_different_ingredients(self, test_bun, ingredient_indices):
        """Тестирует создание бургера с разным количеством ингредиентов"""
        ingredients_list = create_ingredients_list(ingredient_indices)
        burger = create_test_burger(test_bun, ingredients_list)

        assert burger.bun == test_bun
        assert len(burger.ingredients) == len(ingredients_list)

        # Рассчитываем ожидаемую цену с учетом удвоения стоимости булочки
        ingredients_price = sum(ing.get_price() for ing in ingredients_list)
        expected_price = (test_bun.get_price() * 2) + ingredients_price
        assert burger.get_price() == expected_price
