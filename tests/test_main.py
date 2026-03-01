import pytest
from main import Product, Smartphone, LawnGrass, Category


@pytest.fixture
def smartphone1():
    """Фикстура для создания первого смартфона"""
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )

@pytest.fixture
def smartphone2():
    """Фикстура для создания второго смартфона"""
    return Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space"
    )

@pytest.fixture
def grass1():
    """Фикстура для создания первой газонной травы"""
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )

@pytest.fixture
def grass2():
    """Фикстура для создания второй газонной травы"""
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый"
    )

def test_smartphone_creation(smartphone1):
    """Тест создания объекта Smartphone"""
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.price == 180000.0
    assert smartphone1.efficiency == 95.5
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"

def test_lawngrass_creation(grass1):
    """Тест создания объекта LawnGrass"""
    assert grass1.name == "Газонная трава"
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"

def test_smartphone_addition(smartphone1, smartphone2):
    """Тест сложения двух смартфонов"""
    result = smartphone1 + smartphone2
    assert isinstance(result, Smartphone)
    assert "Samsung Galaxy S23 Ultra + Iphone 15" in result.name
    assert result.price == 390000.0  # 180000 + 210000
    assert result.quantity == 13  # 5 + 8
    assert abs(result.efficiency - 96.85) < 0.01  # (95.5 + 98.2) / 2
    assert "S23 Ultra + 15" in result.model
    assert result.memory == 768  # 256 + 512

def test_lawngrass_addition(grass1, grass2):
    """Тест сложения двух видов газонной травы"""
    result = grass1 + grass2
    assert isinstance(result, LawnGrass)
    assert "Газонная трава + Газонная трава 2" in result.name
    assert result.price == 950.0  # 500 + 450
    assert result.quantity == 35  # 20 + 15
    assert "Россия + США" in result.country
    assert "Среднее: 7 дней и 5 дней" in result.germination_period

def test_addition_different_types(smartphone1, grass1):
    """Тест попытки сложения разных типов товаров"""
    with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
        smartphone1 + grass1

def test_category_creation():
    """Тест создания категории"""
    category = Category("Смартфоны", "Высокотехнологичные смартфоны")
    assert category.name == "Смартфоны"
    assert category.description == "Высокотехнологичные смартфоны"
    assert len(category.products) == 0
