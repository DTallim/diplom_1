import pytest
from conftest import test_bun
from praktikum.bun import Bun



class TestBun:
    def test_bun_creation(self, test_bun):
        """Проверка создания булочки с валидными параметрами"""
        assert test_bun.get_name() == "test bun"
        assert test_bun.get_price() == 100.0

    def test_bun_type_validation(self, test_bun):
        """Проверка типов данных булочки"""
        assert isinstance(test_bun.get_name(), str)
        assert isinstance(test_bun.get_price(), float)

    def test_bun_name_immutability(self):
        """Проверка неизменяемости имени булочки"""
        name = "test bun"
        bun = Bun(name, 100.0)
        name = "changed name"
        assert bun.get_name() == "test bun"

    def test_bun_price_immutability(self):
        """Проверка неизменяемости цены булочки"""
        price = 100.0
        bun = Bun("test bun", price)
        price = 200.0
        assert bun.get_price() == 100.0

    @pytest.mark.parametrize("price", [1.0, 100.0, 1000.0])
    def test_bun_price_values(self, price):
        """Проверка различных значений цены"""
        bun = Bun("test bun", price)
        assert bun.get_price() == price

    @pytest.mark.parametrize("name", ["short", "normal name", "very long name"])
    def test_bun_name_values(self, name):
        """Проверка различных значений имени"""
        bun = Bun(name, 100.0)
        assert bun.get_name() == name

    def test_bun_str_representation(self, test_bun):
        """Проверка строкового представления булочки"""
        assert str(test_bun)
        assert isinstance(str(test_bun), str)

    def test_bun_creation_basic(self):
        """Базовая проверка создания булочки"""
        bun = Bun("test bun", 100.0)
        assert bun is not None
        assert hasattr(bun, 'get_name')
        assert hasattr(bun, 'get_price')

    def test_bun_get_methods(self):
        """Проверка методов получения данных"""
        bun = Bun("test bun", 100.0)
        assert callable(bun.get_name)
        assert callable(bun.get_price)
        assert bun.get_name() == "test bun"
        assert bun.get_price() == 100.0