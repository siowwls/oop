from typing import Any


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: Any, description: Any, price: Any, quantity: Any) -> None:
        self.name = name  # название
        self.description = description  # описание
        self.__price = price
        self.quantity = quantity  # количество товара в наличии
        self.summa = self.__price * self.quantity  #цену умножаем на кол-во

    def __str__(self) -> str:
        return f'{self.name}, {int(self.__price)} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other) -> int:
        return int(self.summa + other.summa)

    @classmethod
    def new_product(cls, information: dict) -> Any:
        """
        Возвращает информацию на основе ссылки на класс.
        """
        return cls(
            information["name"],
            information["price"],
            information["description"],
            information["quantity"],
        )

    @property
    def price_1(self) -> Any:
        """
        Возвращает приватизированную цену.
        """
        return self.__price

    @price_1.setter
    def price_1(self, price: float) -> None:
        """
        Сравнивает приватизированную цену с условием и присваивает новое значение.
        """
        if price > 0:
            self.__price = price
        else:
            raise ValueError("Цена не должна быть нулевая или отрицательная")


product_1 = Product("помидор", "помидор cherry", 15.0, 100)

product_2 = Product("огурцы", "огурцы малосольные", 25.0, 100)

print(product_1)

