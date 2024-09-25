from typing import Any


class Product:
    def __init__(self, name: Any, description: Any, price: Any, quantity: Any) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: Any, description: Any) -> None:
        self.name = name
        self.description = description
        self.products: list = []
        Category.total_categories += 1

    def add_product(self, product: Any) -> None:
        if isinstance(product, Product):
            self.products.append(product)
            Category.total_products += 1
        else:
            raise ValueError

    def __str__(self) -> str:
        product_list = ", ".join([product.name for product in self.products])
        return f"Category(name={self.name}, description={self.description}, products=[{product_list}], " \
               f"total_products={len(self.products)})"


if __name__ == "__main__":
    pr1 = Product("Laptop", "High performance laptop", 1200.99, 5)
    pr2 = Product("Smartphone", "Latest model smartphone", 799.99, 10)

    electronics_category = Category("Electronics", "Devices and gadgets")

    electronics_category.add_product(pr1)
    electronics_category.add_product(pr2)
