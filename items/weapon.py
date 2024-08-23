from characters.character import Character
from .item import Item

class Weapon(Item):
    def __init__(self, name, owner, weight: int, durability: int, damage: int):
        super().__init__('weapon', name, owner, weight, durability)
        self.__damage = damage

    def damage(self):
        return self.__damage

    def use(self, target: Character):
        super().use()
        target.damage(self.__damage)

    def __str__(self):
        return f'{super().__str__()} - {self.damage()} damage'