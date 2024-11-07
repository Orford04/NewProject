from enum import Enum


class Container(str, Enum):
    DISH = "Dish"
    CAKE_CONE = "Cake Cone"
    WAFFLE_CONE = "Waffle Cone"

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)