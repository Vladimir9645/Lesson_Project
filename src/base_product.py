from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_description(self) -> str:
        """Должен быть реализован в дочерних классах."""
        pass

    def display_info(self):
        """Выводит основную информацию о продукте."""
        print(f"Товар: {self.name}")
        print(f"Описание: {self.description}")
        print(f"Цена: {self.price} руб.")
        print(f"Количество: {self.quantity} шт.")
