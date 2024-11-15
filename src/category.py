from typing import Any

from src.product import Product


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

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self.__products)} шт.'

    def add_product(self, private_product: Product) -> None:
        """
        Функция добавляет продукты в приватный список
        """
        self.__products.append(private_product)
        Category.count_products += 1

    @property
    def products_1(self) -> list:
        """
        Возвращает список продуктов.
        """
        return self.__products

    @property
    def get_inf_products(self) -> str:
        """
        Информация о товаре
        """
        inf_products = []
        for product in self.__products:
            inf_products.append(
                f"{str(product)}"
            )
        return " ".join(inf_products)


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # print(product2)
    category = Category("TEXIKA", "TEXIKA")
    category.add_product(product3)
    category.add_product(product1)
    category.add_product(product2)
    print(category)
