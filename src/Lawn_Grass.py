from src.Product import Product


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def _create_product(self, other):
        return LawnGrass(
            f"{self.name} + {other.name}",
            f"Объединённая газонная трава: {self.description} и {other.description}",
            self.price + other.price,
            self.quantity + other.quantity,
            f"{self.country} + {other.country}",  # объединение стран-производителей
            f"Среднее: {self.germination_period} и {other.germination_period}",  # усреднение сроков прорастания
            f"{self.color} + {other.color}"  # объединение цветов
        )
