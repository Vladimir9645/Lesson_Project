import pytest
from abc import ABC
from src.base_product import BaseProduct
from src.product import Product  # импортируем дочерний класс

class TestBaseProduct:
    def test_abstract_class(self):
        """Проверяет, что BaseProduct — абстрактный класс."""
        assert issubclass(BaseProduct, ABC)

    def test_init_attributes_through_child(self):
        """Проверяет инициализацию атрибутов через дочерний класс."""
        # Создаём экземпляр дочернего класса Product
        product = Product("Test Product", "Description", 100.0, 5)

        # Проверяем, что атрибуты инициализированы корректно
        assert product.name == "Test Product"
        assert product.description == "Description"
        assert product.price == 100.0
        assert product.quantity == 5

    def test_get_description_abstract(self):
        """Проверяет, что get_description — абстрактный метод."""
        with pytest.raises(TypeError):
            BaseProduct("Test", "Desc", 100, 5)
            