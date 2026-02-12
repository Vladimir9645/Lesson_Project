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

class TestProducts:
    @pytest.fixture
    def product1(self):
        return Product("Test Phone 1", "Description 1", 10000.0, 5)

    @pytest.fixture
    def product2(self):
        return Product("Test Phone 2", "Description 2", 15000.0, 3)

    def test_add_magic_method(self, product1, product2):
        """Тест метода __add__: сумма стоимости двух продуктов"""
        expected_total = product1.price * product1.quantity + product2.price * product2.quantity
        result = product1 + product2
        assert result == expected_total

    def test_str_magic_method(self, product1):
        """Тест метода __str__: строковое представление продукта"""
        expected_str = "Test Phone 1, 10000.0 руб. Остаток: 5 шт."
        assert str(product1) == expected_str


    def test_price_setter_valid_value(self, product1):
        """Тест сеттера цены с корректным значением"""
        product1.price = 12000.0
        assert product1.price == 12000.0

class TestCategory:
    @pytest.fixture
    def products(self):
        return [
            Product("Phone A", "Desc A", 10000.0, 2),
            Product("Phone B", "Desc B", 15000.0, 4),
        ]

    @pytest.fixture
    def category(self, products):
        return Category("Test Category", "Test Description", products)

    def test_str_magic_method_with_products(self, category):
        """Тест метода __str__ для категории с продуктами"""
        expected_output = (
            "Phone A, 10000.0 руб. Остаток: 2 шт.\n"
            "Phone B, 15000.0 руб. Остаток: 4 шт.\n"
        )
        assert str(category) == expected_output

    def test_str_magic_method_empty_category(self):
        """Тест метода __str__ для категории без продуктов"""
        empty_category = Category("Empty Category", "Empty Description", [])
        assert str(empty_category) == ""