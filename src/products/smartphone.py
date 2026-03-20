from ..product import Product

class Смартфон(Product):
    """Класс для представления смартфонов."""

    def __init__(self, name: str, description: str, price: float, quantity: int, brand: str, memory: str):
        super().__init__(name, description, price, quantity)
        self.brand = brand
        self.memory = memory

    def get_description(self) -> str:
        return (f"Смартфон {self.name} от {self.brand}, память: {self.memory}, "
                f"описание: {self.description}, цена: {self.price} руб., "
                f"количество: {self.quantity} шт.")

