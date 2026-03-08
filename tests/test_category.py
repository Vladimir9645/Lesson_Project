import pytest
from src.category import Category
from src.product import Product

class TestCategory:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Автоматически сбрасывает счётчики перед каждым тестом."""
        Category.reset_counters()
        yield  # выполняем тест
        # здесь можно добавить код после теста, если нужно

    @pytest.fixture
    def setup_products(self):
        """Фикстура для создания тестовых продуктов."""
        return [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 3),
        ]

    def test_category_creation(self):
        """Проверяет создание категории."""
        category = Category("Electronics", "Electronic devices", [])
        assert category.name == "Electronics"
        assert category.description == "Electronic devices"
        assert len(category.products) == 0
        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_category_counters(self, setup_products):
        """Проверяет счётчики категорий и продуктов."""
        # Создаём первую категорию
        category1 = Category("Смартфоны", "Мобильные устройства", setup_products[:2])
        assert Category.category_count == 1
        assert Category.product_count == 2

        # Создаём вторую категорию
        product3 = Product("Product 3", "Desc 3", 150.0, 4)
        category2 = Category("Телевизоры", "TV devices", [product3])
        assert Category.category_count == 2
        assert Category.product_count == 3

    def test_add_product(self):
        """Проверяет добавление продукта в категорию."""
        category = Category("Test Category", "Test Description", [])
        product = Product("New Product", "New Desc", 300.0, 10)

        category.add_product(product)
        assert len(category.products) == 1
        assert product in category.products
        assert Category.product_count == 1

    def test_len_method(self, setup_products):
        """Проверяет работу метода __len__."""
        category = Category("Test", "Desc", setup_products)
        assert len(category) == 2