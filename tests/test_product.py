import pytest
from src.product import Product

class TestProduct:
    def test_product_creation(self, capsys):
        """Проверяет создание продукта и логирование."""
        product = Product("Test Product", "Description", 100.0, 5)
        captured = capsys.readouterr()

        # Проверяем логирование
        assert "Создан объект класса Product" in captured.out

        # Проверяем атрибуты
        assert product.name == "Test Product"
        assert product.description == "Description"
        assert product.price == 100.0
        assert product.quantity == 5

    def test_get_description(self):
        """Проверяет метод get_description."""
        product = Product("Test Product", "Description", 100.0, 5)
        description = product.get_description()
        expected = "Test Product - Description, цена: 100.0 руб., количество: 5 шт."
        assert description == expected

    def test_display_info(self, capsys):
        """Проверяет метод display_info."""
        product = Product("Test Product", "Description", 100.0, 5)
        product.display_info()
        captured = capsys.readouterr()

        assert "Товар: Test Product" in captured.out
        assert "Описание: Description" in captured.out
        assert "Цена: 100.0 руб." in captured.out
        assert "Количество: 5 шт." in captured.out

    def test_product_with_zero_quantity_raises_value_error(self):
        """Тест: создание продукта с нулевым количеством вызывает ValueError"""
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            Product("Бракованный товар", "Неверное количество", 1000.0, 0)

    def test_product_with_negative_quantity_raises_value_error(self):
        """Тест: создание продукта с отрицательным количеством вызывает ValueError"""
        with pytest.raises(ValueError, match="Товар с отрицательным количеством не может быть добавлен"):
            Product("Телефон", "Описание", 1000.0, -1)
