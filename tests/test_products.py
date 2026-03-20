import pytest
from src.products.smartphone import Смартфон
from src.products.lawn_grass import ТраваГазонная

class TestSmartphone:
    def test_smartphone_creation(self, capsys):
        """Проверяет создание смартфона."""
        smartphone = Смартфон(
            "Galaxy S23",
            "256GB, Серый",
            79990.0,
            5,
            "Samsung",
            "256GB"
        )
        captured = capsys.readouterr()

        assert "Создан объект класса Смартфон" in captured.out
        assert smartphone.brand == "Samsung"
        assert smartphone.memory == "256GB"

    def test_smartphone_description(self):
        """Проверяет описание смартфона."""
        smartphone = Смартфон("Galaxy S23", "256GB, Серый", 79990.0, 5, "Samsung", "256GB")
        description = smartphone.get_description()
        assert "Смартфон Galaxy S23 от Samsung" in description
        assert "память: 256GB" in description

class TestLawnGrass:
    def test_lawn_grass_creation(self, capsys):
        """Проверяет создание газонной травы."""
        grass = ТраваГазонная(
            "Изумрудный луг",
            "Семена для газона",
            1500.0,
            10,
            50.0,
            "мятлик"
        )
        captured = capsys.readouterr()

        assert "Создан объект класса ТраваГазонная" in captured.out
        assert grass.area_coverage == 50.0
        assert grass.seed_type == "мятлик"

    def test_lawn_grass_description(self):
        """Проверяет описание газонной травы."""
        grass = ТраваГазонная("Изумрудный луг", "Семена для газона", 1500.0, 10, 50.0, "мятлик")
        description = grass.get_description()
        assert "Газонная трава" 'Изумрудный луг'
