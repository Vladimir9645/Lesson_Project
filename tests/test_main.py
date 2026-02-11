import pytest
from main import Product, Category  # замените yourmodule на имя вашего файла


class TestProduct:
    def test_product_creation(self):
        """Тест создания продукта с корректными данными"""
        product = Product("Test Phone", "Test description", 1000.0, 10)
        assert product.name == "Test Phone"
        assert product.description == "Test description"
        assert product.price == 1000.0
        assert product.quantity == 10

    def test_price_getter(self):
        """Тест геттера цены"""
        product = Product("Test", "Desc", 500.0, 5)
        assert product.price == 500.0

    def test_price_setter_positive(self):
        """Тест установки положительной цены"""
        product = Product("Test", "Desc", 500.0, 5)
        product.price = 600.0
        assert product.price == 600.0

    def test_price_setter_negative(self, capsys):
        """Тест установки отрицательной цены"""
        product = Product("Test", "Desc", 500.0, 5)
        product.price = -100.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 500.0  # цена не изменилась

    def test_price_setter_zero(self, capsys):
        """Тест установки нулевой цены"""
        product = Product("Test", "Desc", 500.0, 5)
        product.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 500.0  # цена не изменилась

    def test_new_product_classmethod(self):
        """Тест класс‑метода new_product"""
        product_data = {
            "name": "Test Product",
            "description": "Test desc",
            "price": 700.0,
            "quantity": 3,
        }
        product = Product.new_product(product_data)
        assert isinstance(product, Product)
        assert product.name == "Test Product"
        assert product.price == 700.0

    def test_product_count_increment(self):
        """Тест увеличения счётчика продуктов"""
        initial_count = Product.product_count
        Product("Test", "Desc", 100.0, 1)
        assert Product.product_count == initial_count + 1


class TestCategory:
    def setup_method(self):
        """Подготовка тестовых данных перед каждым тестом"""
        self.product1 = Product("Phone 1", "Desc 1", 1000.0, 5)
        self.product2 = Product("Phone 2", "Desc 2", 2000.0, 3)
        self.category = Category("Test Category", "Test Desc", [self.product1])

    def test_category_creation(self):
        """Тест создания категории"""
        assert self.category.name == "Test Category"
        assert len(self.category._Category__products) == 1

    def test_products_getter_format(self):
        """Тест формата вывода геттера products"""
        result = self.category.products
        expected_line = f"{self.product1.name}, {self.product1.price} руб. Остаток: {self.product1.quantity} шт.\n"
        assert expected_line in result

    def test_add_product(self):
        """Тест добавления продукта в категорию"""
        initial_product_count = Product.product_count
        initial_products_count = len(self.category._Category__products)
        self.category.add_product(self.product2)
        assert len(self.category._Category__products) == initial_products_count + 1
        assert Product.product_count == initial_product_count + 1

    def test_category_count_increment(self):
        """Тест увеличения счётчика категорий"""
        initial_count = Category.category_count
        Category("New Cat", "Desc", [])
        assert Category.category_count == initial_count + 1
