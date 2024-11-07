from enum import Enum


class Topping(str, Enum):
    CHOCOLATE = "Chocolate"
    WHIPPED_CREAM = "Whipped Cream"
    CHERRY = "Cherry"
    CARAMEL = "Caramel"
    PEANUTS = "Peanuts"

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)