from src.Product import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def _create_product(self, other):
        return Smartphone(
            f"{self.name} + {other.name}",
            f"Объединённый смартфон: {self.description} и {other.description}",
            self.price + other.price,
            self.quantity + other.quantity,
            (self.efficiency + other.efficiency) / 2,  # среднее значение производительности
            f"{self.model} + {other.model}",  # объединение моделей
            self.memory + other.memory,  # суммарный объём памяти
            f"{self.color} + {other.color}"  # объединение цветов
        )