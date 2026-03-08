from typing import List, Optional


class Category:
    category_count = 0
    product_count = 0

    @classmethod
    def reset_counters(cls):
        """Сбрасывает счётчики категорий и продуктов."""
        cls.category_count = 0
        cls.product_count = 0

    def __init__(self, name: str, description: str, products: Optional[List] = None):
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
