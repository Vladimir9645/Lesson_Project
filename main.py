class Product:
    product_count = 0  # Атрибут класса: общее число продуктов

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity
        # Увеличиваем счётчик при создании объекта
        Product.product_count += 1

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, value: float):
        """Сеттер для атрибута цены с проверкой на положительное значение"""
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data: dict) -> Product:
        """Класс‑метод для создания продукта из словаря"""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )


class Category:
    category_count = 0  # Атрибут класса: общее число категорий
    product_count = 0  # Атрибут класса: счётчик продуктов во всех категориях

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут списка товаров
        # Увеличиваем счётчик при создании объекта
        Category.category_count += 1
        # Увеличиваем общий счетчик продуктов на кол-ло переданных продуктов
        Category.product_count += len(products)

    @property
    def products(self):
        return self.__products

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def add_product(self, product: Product):
        """Метод для добавления продукта в приватный атрибут __products.
        Прибавляет 1 к счётчику продуктов класса Product."""
        self.__products.append(product)
        Category.product_count += 1  # Увеличиваем общий счётчик продуктов
        Product.product_count += 1

    def total_cost(self):
        return sum(p.price * p.quantity for p in self.products)



if __name__ == "__main__":
    # Создаём продукты
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0, 5
    )

    product2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0, 8
    )

    product3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0, 14
    )

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(product1))
    print(str(product2))
    print(str(product3))
    print()
    print(str(category1))

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    print ("Общая стоимость категорий:", category1.total_cost())
