from  src.product import Product


class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

    def middle_price(self):
        if not self.products:
            return 0
        total_price = sum(product.price for product in self.products)
        return total_price / len(self.products)
