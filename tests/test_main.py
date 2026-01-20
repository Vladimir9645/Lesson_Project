from src.main import Product, Category


class TestProduct:
    def test_product_initialization(self):
        """Проверка создания экземпляра Product."""
        product = Product("Test Phone", "A test product", 10000.0, 5)
        assert product.name == "Test Phone"
        assert product.description == "A test product"
        assert product.price == 10000.0
        assert product.quantity == 5

    def test_product_count_increments(self):
        """Счётчик product_count увеличивается при создании нового Product."""
        # Исходное значение
        initial_count = Product.product_count

        # Создаём продукт
        product = Product("Another Phone", "Second test", 8000.0, 3)

        # Проверяем, что счётчик вырос на 1
        assert Product.product_count == initial_count + 1


class TestCategory:
    def test_category_initialization(self):
        """Проверка создания экземпляра Category."""
        products = [
            Product("P1", "Desc 1", 100.0, 2),
            Product("P2", "Desc 2", 200.0, 1)
        ]
        category = Category("Electronics", "Gadgets and stuff", products)

        assert category.name == "Electronics"
        assert category.description == "Gadgets and stuff"
        assert len(category.products) == 2
        assert category.products[0].name == "P1"
        assert category.products[1].name == "P2"

    def test_category_count_increments(self):
        """Счётчик category_count увеличивается при создании новой Category."""
        initial_count = Category.category_count

        Category("Toys", "For kids", [])

        assert Category.category_count == initial_count + 1





