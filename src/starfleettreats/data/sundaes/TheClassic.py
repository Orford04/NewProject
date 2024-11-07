from typing import List, Set
from src.starfleettreats.data.enums.Container import Container
from src.starfleettreats.data.enums.Topping import Topping

class TheClassic:

    def __init__(self) -> None:
        self.__container: Container = Container.WAFFLE_CONE
        self.__vanilla: bool = True
        self.__banana: bool = True
        self.__toppings: Set(Topping) = {Topping.CHOCOLATE,
                                         Topping.WHIPPED_CREAM,
                                         Topping.CHERRY}
    

    @property
    def price(self) -> float:
        return 5.50

    @property
    def calories(self) -> int:
        return 1050

    @property
    def container(self) -> Container:
        return self.__container

    @container.setter
    def container(self, value: Container)-> None:
        self.__container = value

    @property
    def vanilla(self) -> bool:
        return self.__vanilla

    @vanilla.setter
    def vanilla(self, value: bool) -> None:
        self.__vanilla = value

    @property
    def banana(self) -> bool:
        return self.__banana

    @banana.setter
    def banana(self, value: bool) -> None:
        self.__banana = value

    @property
    def toppings(self) -> set(Topping):
        return self.__toppings.copy()

    def add_topping(self, value: Topping) -> None:
        self.__toppings.add(value)

    def remove_topping(self, value: Topping) -> None:
        self.__toppings.remove(value)

    @property
    def special_instructions(self) -> List[str]:
        specials: List[str] = []
        if not self.__vanilla:
            specials.append("Hold Vanilla")
        if not self.__banana:
            specials.append("Hold Banana")
        return specials

    def __str__(self) -> str:
        return "The Classic in a {}".format(self.__container)
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, TheClassic):
            return (self.__container == value.container and
                    self.__vanilla == value.vanilla and
                    self.__banana == value.banana and
                    self.__toppings == value.toppings)
        else:
            False