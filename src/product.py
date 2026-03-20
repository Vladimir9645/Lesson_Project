from .base_product import BaseProduct
from .mixins import CreationLoggerMixin


class Product(CreationLoggerMixin, BaseProduct):
    """Промежуточный класс продукта с логированием создания."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        # Проверяем, что кол-во товара не равно нулю
        if quantity <= 0:
            if quantity == 0:
                raise ValueError("Товар с нулевым количеством не может быть добавлен")
            else:  # quantity < 0
                raise ValueError(
                    "Товар с отрицательным количеством не может быть добавлен"
                )

        # Если првоверка пройдена, вызываем инициализатор родительского класса
        super().__init__(name, description, price, quantity)

    def get_description(self) -> str:
        return f"{self.name} - {self.description}, цена: {self.price} руб., количество: {self.quantity} шт."
