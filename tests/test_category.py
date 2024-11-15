import pytest

from src.category import Category
from src.product import product_1, Product


@pytest.fixture
def category_1() -> Category:
    return Category("Продукты", "Овощи")


def test_private_products_access() -> None:
    category = Category("Продукты", "Овощи")
    with pytest.raises(AttributeError):
        _ = category.__products


def test_category_info(category_1: Category) -> None:
    assert category_1.name == "Продукты"
    assert category_1.description == "Овощи"


def test_get_inf_products(category_1: Category) -> None:
    category_1.add_product(product_1)
    assert category_1.get_inf_products == "помидор, 15 руб. Остаток: 100 шт."


def test_str() -> None:
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category("TEXIKA", "TEXIKA")
    category.add_product(product3)
    assert str(category) == "TEXIKA, количество продуктов: 1 шт."
