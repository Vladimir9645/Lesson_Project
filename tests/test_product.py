import pytest
from src import Product

class TestProduct:
    def test_product_creation_valid(self):
        """Тест создания продукта с корректными данными"""
        product = Product("Смартфон", "Описание", 1000.0, 5)
        assert product.name == "Смартфон"
        assert product.description == "Описание"
        assert product.price == 1000.0
        assert product.quantity == 5

    def test_product_creation_zero_quantity(self):
        """Тест создания продукта с нулевым количеством — должна выброситься ошибка"""
        with pytest.raises(ValueError) as excinfo:
            Product("Бракованный товар", "Неверное количество", 1000.0, 0)
        assert str(excinfo.value) == "Товар с нулевым количеством не может быть добавлен"

    def test_product_creation_negative_quantity(self):
        """Тест создания продукта с отрицательным количеством"""
        # По заданию проверка только на ноль, но проверим поведение
        product = Product("Товар", "Описание", 500.0, -1)
        assert product.quantity == -1

    def test_product_attributes_access(self):
        """Тест доступа к атрибутам продукта"""
        product = Product("Ноутбук", "Мощный ноутбук", 50000.0, 3)
        assert hasattr(product, 'name')
        assert hasattr(product, 'description')
        assert hasattr(product, 'price')
        assert hasattr(product, 'quantity')