from ..product import Product

class ТраваГазонная(Product):
    """Класс для представления газонной травы."""

    def __init__(self, name: str, description: str, price: float, quantity: int, area_coverage: float, seed_type: str):
        super().__init__(name, description, price, quantity)
        self.area_coverage = area_coverage
        self.seed_type = seed_type

    def get_description(self) -> str:
        return (f"Газонная трава '{self.name}', тип семян: {self.seed_type}, "
                f"покрывает площадь {self.area_coverage} м², описание: {self.description}, "
                f"цена: {self.price} руб., количество: {self.quantity} упаковок")