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
    def products(self) -> str:
        """Геттер для приватного атрибута products.
        Возвращает строку со всеми продуктами по шаблону:
        'Название продукта, X руб. Остаток: X шт.\n'"""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    def add_product(self, product: Product):
        """Метод для добавления продукта в приватный атрибут __products.
        Прибавляет 1 к счётчику продуктов класса Product."""
        self.__products.append(product)
        Category.product_count += 1  # Увеличиваем общий счётчик продуктов



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

    product4 = Product(
        "55\" QLED 4K",
        "Фоновая подсветка",
        123000.0, 7
    )

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    category1.add_product(product4)
    print(category1.products)
    print(Category.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra",
         "description": "256GB, Серый цвет, 200MP камера",
         "price": 180000.0,
         "quantity": 5}
    )

    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100  # Выведет сообщение об ошибке
    print(new_product.price)
    new_product.price = 0  # Выведет сообщение об ошибке
    print(new_product.price)

