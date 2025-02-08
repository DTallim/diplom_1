# helpers.py

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import EXPECTED_RECEIPT_TEMPLATE


def validate_price(price):
    """
    Проверяет корректность цены

    Args:
        price (float): цена для проверки
    Returns:
        bool: True если цена корректна
    """
    return isinstance(price, float) and price > 0


def validate_name(name):
    """
    Проверяет корректность имени

    Args:
        name (str): имя для проверки
    Returns:
        bool: True если имя корректно
    """
    return isinstance(name, str) and name.strip() != ""


def validate_ingredient_type(type_):
    """
    Проверяет корректность типа ингредиента

    Args:
        type_ (str): тип для проверки
    Returns:
        bool: True если тип корректен
    """
    return type_ in [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]


def create_test_burger(bun=None, ingredients=None):
    """
    Создает тестовый бургер с указанной булочкой и ингредиентами

    Args:
        bun (Bun, optional): булочка для бургера
        ingredients (list, optional): список ингредиентов
    Returns:
        Burger: созданный бургер
    """
    burger = Burger()
    if bun:
        burger.set_buns(bun)
    if ingredients:
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
    return burger


def format_receipt(bun_name, ingredients, total_price):
    """
    Форматирует чек по шаблону

    Args:
        bun_name (str): название булочки
        ingredients (list): список ингредиентов
        total_price (float): итоговая цена
    Returns:
        str: отформатированный чек
    """
    ingredients_text = '\n'.join([
        f"= {ing.get_type().lower()} {ing.get_name()} ="
        for ing in ingredients
    ]) if ingredients else ""

    return EXPECTED_RECEIPT_TEMPLATE.format(
        bun_name=bun_name,
        ingredients=ingredients_text,
        total_price=total_price
    )


def calculate_burger_price(bun, ingredients):
    """
    Вычисляет ожидаемую цену бургера

    Args:
        bun (Bun): булочка
        ingredients (list): список ингредиентов
    Returns:
        float: итоговая цена
    """
    return (bun.get_price() * 2 +  # верх и низ бургера
            sum(ing.get_price() for ing in (ingredients or [])))

