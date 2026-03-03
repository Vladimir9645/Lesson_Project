class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных типов")
        return self._create_product(other)

    def _create_product(self, other):
        """Базовый метод для создания объединённого продукта — переопределяется в наследниках"""
        return self.__class__(
            f"{self.name} + {other.name}",
            f"Объединённый товар: {self.description} и {other.description}",
            self.price + other.price,
            self.quantity + other.quantity
        )
