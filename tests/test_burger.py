import pytest
from helpers import (
    create_test_burger,
    format_receipt,
    create_ingredients_list
)


class TestBurger:
    def test_empty_burger(self, empty_burger):
        """Тестирует создание пустого бургера"""
        assert empty_burger.bun is None
        assert len(empty_burger.ingredients) == 0

    def test_burger_with_bun(self, test_bun):
        """Тестирует создание бургера только с булочкой"""
        burger = create_test_burger(bun=test_bun)
        assert burger.bun == test_bun
        assert len(burger.ingredients) == 0
        assert burger.get_price() == test_bun.get_price() * 2

    def test_burger_with_one_ingredient(self, test_bun, test_filling):
        """Тестирует создание бургера с одним ингредиентом"""
        ingredients_list = [test_filling]
        burger = create_test_burger(test_bun, ingredients_list)

        assert burger.bun == test_bun
        assert len(burger.ingredients) == 1
        expected_price = (test_bun.get_price() * 2) + test_filling.get_price()
        assert burger.get_price() == expected_price

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
        assert actual_receipt == expected_receipt

    @pytest.mark.parametrize("ingredient_indices", [
        [],
        [1],
        [1, 4]
    ])
    def test_burger_with_different_ingredients(self, test_bun, ingredient_indices):
        """Тестирует создание бургера с разным количеством ингредиентов"""
        ingredients_list = create_ingredients_list(ingredient_indices)
        burger = create_test_burger(test_bun, ingredients_list)

        assert burger.bun == test_bun
        assert len(burger.ingredients) == len(ingredients_list)

        ingredients_price = sum(ing.get_price() for ing in ingredients_list)
        expected_price = (test_bun.get_price() * 2) + ingredients_price
        assert burger.get_price() == expected_price

    def test_remove_ingredient(self, test_bun, test_filling, test_sauce):
        """Тестирует удаление ингредиента из бургера"""
        ingredients_list = [test_filling, test_sauce]
        burger = create_test_burger(test_bun, ingredients_list)

        # Проверяем начальное состояние
        assert len(burger.ingredients) == 2
        initial_price = burger.get_price()

        # Удаляем ингредиент
        removed_ingredient = burger.remove_ingredient(0)

        # Проверяем, что вернулся правильный ингредиент
        assert removed_ingredient == test_filling

        # Проверяем, что ингредиент удален
        assert len(burger.ingredients) == 1
        assert test_filling not in burger.ingredients
        assert test_sauce in burger.ingredients

        # Проверяем, что цена уменьшилась на стоимость удаленного ингредиента
        assert burger.get_price() == initial_price - test_filling.get_price()

    def test_remove_ingredient_empty_burger(self, test_bun):
        """Тестирует удаление ингредиента из пустого бургера"""
        burger = create_test_burger(test_bun)

        # Проверяем, что при попытке удалить ингредиент из пустого бургера возвращается None
        assert burger.remove_ingredient(0) is None
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, test_bun, test_filling, test_sauce):
        """Тестирует перемещение ингредиента в бургере"""
        ingredients_list = [test_filling, test_sauce]
        burger = create_test_burger(test_bun, ingredients_list)

        # Проверяем начальное положение
        assert burger.ingredients[0] == test_filling
        assert burger.ingredients[1] == test_sauce

        # Перемещаем ингредиент с индекса 0 на позицию 1
        burger.move_ingredient(0, 1)

        # Проверяем, что ингредиенты поменялись местами
        assert burger.ingredients[0] == test_sauce
        assert burger.ingredients[1] == test_filling

        # Проверяем, что количество ингредиентов не изменилось
        assert len(burger.ingredients) == 2

    def test_move_ingredient_invalid_positions(self, test_bun, test_filling):
        """Тестирует перемещение ингредиента на некорректную позицию"""
        ingredients_list = [test_filling]
        burger = create_test_burger(test_bun, ingredients_list)

        # Пытаемся переместить на несуществующую позицию
        burger.move_ingredient(0, 5)

        # Проверяем, что ингредиент остался на месте
        assert burger.ingredients[0] == test_filling
        assert len(burger.ingredients) == 1