import pytest
from io import StringIO
import sys
from src.mixins import CreationLoggerMixin

class MockProduct(CreationLoggerMixin):
    def __init__(self, name, description, price, quantity):
        # Сами инициализируем атрибуты
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        # Вызываем родительский __init__ для активации логирования
        super().__init__(name, description, price, quantity)

class TestCreationLoggerMixin:
    def test_logger_output(self, capsys):
        """Проверяет вывод логгера при создании объекта."""
        product = MockProduct("Test Product", "Description", 100.0, 5)
        captured = capsys.readouterr()

        assert "Создан объект класса MockProduct" in captured.out
        assert "name='Test Product'" in captured.out
        assert "price=100.0" in captured.out
        assert "quantity=5" in captured.out