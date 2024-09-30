import pytest

from src.category import Category
from src.product import product_1, product_2


@pytest.fixture
def category_1() -> Category:
    return Category("Продукты", "Овощи", [product_1, product_2])


def test_category_info(category_1: Category) -> None:
    assert category_1.name == "Продукты"
    assert category_1.description == "Овощи"
    assert category_1.products == [product_1, product_2]
