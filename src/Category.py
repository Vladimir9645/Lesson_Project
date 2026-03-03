from src.Product import Product


class Category:
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = []
        if products:
            for product in products:
                self.add_product(product)

    @property
    def products(self):
        return self._products

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self._products.append(product)
        Category.product_count += 1
