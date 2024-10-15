from typing import Any

from src.product import Product, product_1, product_2


class Category:
    name: str
    description: str
    products: list
    count_category = 0
    count_products = 0

    def __init__(self, name: Any, description: Any) -> None:
        self.name = name  # название категории
        self.description = description  # описание категории
        self.__products: list = []  # список товаров из класса product
        Category.count_category += 1

    def add_product(self, private_product: Product) -> None:
        """
        Функция добавляет продукты в приватный список
        """
        self.__products.append(private_product)
        Category.count_products += 1

    @property
    def get_inf_products(self) -> str:
        """
        Информация о товаре
        """
        inf_products = []
        for product in self.__products:
            inf_products.append(
                f"{product.name}, {product.check_price}руб. Остаток: {product.quantity} штук."
            )
        return " ".join(inf_products)


if __name__ == "__main__":
    category = Category("Продукты", "Овощи")
