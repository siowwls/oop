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

    def add_product(self, private_product: Product) -> None:
        """
        Функция добавляет продукты в приватный список
        """
        self.__products.append(private_product)
        Category.count_products += 1

    @property
    def products_1(self) -> list:
        """
        Возвращает список продуктов
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
                f"{product.name}, {product.price_1}руб. Остаток: {product.quantity} штук."
            )
        return " ".join(inf_products)


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    )

    print(category1.products_1)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products_1)
    print(Category.count_products)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price_1)
    print(new_product.quantity)

    new_product.price_1 = 800
    print(new_product.price_1)

    new_product.price_1 = -100
    print(new_product.price_1)
    new_product.price_1 = 0
    print(new_product.price_1)
