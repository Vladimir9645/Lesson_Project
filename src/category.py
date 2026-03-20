class Category:
    category_count = 0
    product_count = 0

    @classmethod
    def reset_counters(cls):
        """Сбрасывает счётчики категорий и продуктов."""
        cls.category_count = 0
        cls.product_count = 0

    def __init__(self, name: str, description: str, products: list = []):
        self.name = name
        self.description = description
        self.__products = products if products else []

        # Увеличиваем счётчики при создании
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, value):
        if isinstance(value, list):
            self.__products = value
            Category.product_count += len(value)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    def __len__(self):
        return len(self.__products)

    def middle_price(self) -> float:
        """Подсчет срдней цены товаров"""
        # Проверяем, есть ли товары в категории
        if not self.__products:
            return 0.0

        # Сумма всех товаров
        total_price = sum(product.price for product in self.__products)

        # Вычесляем среднюю цену
        average = total_price / len(self.__products)
        return average
