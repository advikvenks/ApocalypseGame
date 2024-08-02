from .item import Item

class Weapon(Item):
    def __init__(self, name, owner, weight, durability, damage):
        super().__init__('weapon', name, owner, weight, durability)
        self.__damage = damage

    def damage(self):
        return self.__damage

    def use(self, target):
        target.damage(self.__damage)

    def __str__(self):
        return f'{super().__str__()} - {self.damage()} damage'