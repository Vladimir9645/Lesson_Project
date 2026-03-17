import pytest
from src import Product, Category


class TestCategory:
    def setup_method(self):
        """Подготовка тестовых данных перед каждым тестом"""
        self.product1 = Product("Samsung", "256GB", 180000.0, 5)
        self.product2 = Product("Iphone", "512GB", 210000.0, 8)
        self.product3 = Product("Xiaomi", "1024GB", 31000.0, 14)
        self.products = [self.product1, self.product2, self.product3]

    def test_category_creation(self):
        """Тест создания категории с продуктами"""
        category = Category("Смартфоны", "Категория смартфонов", self.products)
        assert category.name == "Смартфоны"
        assert category.description == "Категория смартфонов"
        assert category.products == self.products

    def test_middle_price_with_products(self):
        """Тест расчёта средней цены для категории с товарами"""
        category = Category("Смартфоны", "Категория смартфонов", self.products)
        expected_price = (180000.0 + 210000.0 + 31000.0) / 3
        assert category.middle_price() == expected_price

    def test_middle_price_empty_category(self):
        """Тест расчёта средней цены для пустой категории"""
        empty_category = Category("Пустая", "Пустая категория", [])
        assert empty_category.middle_price() == 0

    def test_middle_price_single_product(self):
        """Тест расчёта средней цены для категории с одним товаром"""
        single_product = [Product("Единственный", "Один товар", 5000.0, 1)]
        category = Category("Один товар", "Категория с одним товаром", single_product)
        assert category.middle_price() == 5000.0

    def test_middle_price_large_numbers(self):
        """Тест расчёта средней цены с большими числами"""
        high_price_product = Product("Дорогой", "Очень дорогой", 1000000.0, 2)
        low_price_product = Product("Дешёвый", "Очень дешёвый", 100.0, 10)
        category = Category("Разные цены", "Товары с разными ценами", [high_price_product, low_price_product])
        expected = (1000000.0 + 100.0) / 2
        assert category.middle_price() == expected
