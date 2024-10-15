from typing import Any


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: Any, description: Any, price: Any, quantity: Any) -> None:
        self.name = name  # название
        self.description = description  # описание
        self.__price = price  # цена
        self.quantity = quantity  # количество товара в наличии

    @classmethod
    def new_product(cls, information: Any) -> Any:
        """
        Возвращает информацию на основе ссылки на класс
        """
        return cls(
            information["name"],
            information["price"],
            information["description"],
            information["quantity"],
        )

    @property
    def check_price(self) -> Any:
        """
        Возвращает приватизированную цену
        """
        return self.__price

    @check_price.setter
    def check_price(self, price: float) -> Any:
        """
        Сравнивает приватизированную цену с условием
        """
        if price <= 0:
            return "Цена не должна быть нулевая или отрицательная"


product_1 = Product("помидор", "помидор cherry", 15.0, 100)

product_2 = Product("огурцы", "огурцы малосольные", 25.0, 100)
