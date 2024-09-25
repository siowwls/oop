import pytest

from main import Category, Product
from typing import Any


@pytest.fixture
def setup_category_and_products() -> Any:
    """Создаем объекты для тестирования."""
    category = Category("Electronics", "Devices and gadgets")
    product1 = Product("Laptop", "A powerful laptop.", 999.99, 10)
    product2 = Product("Smartphone", "A latest model smartphone.", 699.99, 20)
    return category, product1, product2


def test_category_initialization(setup_category_and_products: Any) -> None:
    """Проверяем корректность инициализации объектов класса Category."""
    category, _, _ = setup_category_and_products
    assert category.name == "Electronics"
    assert category.description == "Devices and gadgets"
    assert len(category.products) == 0  # Изначально продуктов нет


def test_product_initialization(setup_category_and_products: Any) -> None:
    """Проверяем корректность инициализации объектов класса Product."""
    _, product1, _ = setup_category_and_products
    assert product1.name == "Laptop"
    assert product1.description == "A powerful laptop."
    assert product1.price == 999.99
    assert product1.quantity == 10


def test_product_count(setup_category_and_products: Any) -> None:
    """Проверяем подсчет количества продуктов."""
    category, product1, product2 = setup_category_and_products
    category.add_product(product1)
    category.add_product(product2)

    assert Category.total_products == 2  # Должно быть 2 продукта


def test_category_count() -> None:
    """Проверяем подсчет количества категорий."""
    # category1 = Category("Electronics", "Devices and gadgets")
    # category2 = Category("Books", "Various genres of literature")

    assert Category.total_categories == 2  # Должно быть 2 категории


if __name__ == "__main__":
    pytest.main()
