from .item import Item

class Consumable(Item):
    def __init__(self, name, owner, weight, durability, heal):
        super().__init__('consumable', name, owner, weight, durability)
        self.__heal = heal

    def healAmount(self):
        return self.__heal

    def use(self, target):
        target.heal(self.__heal)