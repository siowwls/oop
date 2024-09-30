import pytest

from src.product import Product


@pytest.fixture
def product_1() -> Product:
    return Product("помидор", "помидор cherry", 15.0, 100)


@pytest.fixture
def product_2() -> Product:
    return Product("огурцы", "огурцы малосольные", 25.0, 100)


def test_info(product_1: Product) -> None:
    assert product_1.name == "помидор"
    assert product_1.description == "помидор cherry"
    assert product_1.price == 15.0
    assert product_1.quantity == 100


def test_info_1(product_2: Product) -> None:
    assert product_2.name == "огурцы"
    assert product_2.description == "огурцы малосольные"
    assert product_2.price == 25.0
    assert product_2.quantity == 100
