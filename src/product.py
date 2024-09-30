from typing import Any


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: Any, description: Any, price: Any, quantity: Any) -> None:
        self.name = name  # название
        self.description = description  # описание
        self.price = price  # цена
        self.quantity = quantity  # количество товара в наличии


product_1 = Product("помидор", "помидор cherry", 15.0, 100)

product_2 = Product("огурцы", "огурцы малосольные", 25.0, 100)
