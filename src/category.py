from typing import Any

from src.product import product_1, product_2


class Category:
    name: str
    description: str
    products: list
    count_category = 0
    count_products = 0

    def __init__(self, name: Any, description: Any, products: Any) -> None:
        self.name = name  # название категории
        self.description = description  # описание категории
        self.products = products  # список товаров из класса product
        Category.count_category += 1
        Category.count_products += 1


if __name__ == "__main__":
    category = Category("Продукты", "Овощи", [product_1, product_2])
