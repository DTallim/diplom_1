from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import EXPECTED_RECEIPT_TEMPLATE, ingredients


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


def validate_ingredient_type(type_: str) -> bool:
    """
    Проверяет корректность типа ингредиента

    Args:
        type_ (str): тип для проверки
    Returns:
        bool: True если тип корректен
    """
    valid_types = [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
    return type_ in valid_types


def create_test_burger(bun: Bun = None, ingredients: list = None) -> Burger:
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



def create_ingredients_list(ingredient_indices: list[int]) -> list:
    """
    Создает список ингредиентов по индексам

    Args:
        ingredient_indices (list[int]): список индексов ингредиентов
    Returns:
        list: список созданных объектов Ingredient
    """
    ingredients_list = []
    for idx in ingredient_indices:
        ing_data = ingredients[idx]
        ingredient_type = (INGREDIENT_TYPE_SAUCE
                           if ing_data[0] == 'SAUCE'
                           else INGREDIENT_TYPE_FILLING)
        ingredient = Ingredient(
            ingredient_type=ingredient_type,
            name=ing_data[1],
            price=float(ing_data[2])
        )
        ingredients_list.append(ingredient)
    return ingredients_list


def validate_buns(buns):
    """Helper function to validate a list of buns"""
    if len(buns) == 0:
        return False

    for bun in buns:
        if not isinstance(bun, Bun):
            return False
        if not bun.get_price() > 0:
            return False
        if not len(bun.get_name()) > 0:
            return False
    return True


def validate_ingredients_by_type(ingredients, ingredient_type):
    """Helper function to validate ingredients of a specific type"""
    filtered_ingredients = [ing for ing in ingredients if ing.get_type() == ingredient_type]
    if len(filtered_ingredients) == 0:
        return False

    for ingredient in filtered_ingredients:
        if not isinstance(ingredient, Ingredient):
            return False
        if not ingredient.get_price() > 0:
            return False
        if not len(ingredient.get_name()) > 0:
            return False
    return True


def get_ingredient_names(ingredients):
    """Helper function to get a list of ingredient names"""
    return [ing.get_name() for ing in ingredients]


def get_bun_names(buns):
    """Helper function to get a list of bun names"""
    return [bun.get_name() for bun in buns]


def count_ingredients_by_type(ingredients, ingredient_type):
    """Helper function to count ingredients of a specific type"""
    return len([ing for ing in ingredients if ing.get_type() == ingredient_type])