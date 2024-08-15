from characters.character import Character
from .item import Item

class Weapon(Item):
    def __init__(self, name, owner, weight: int, durability: int, damage: int):
        super().__init__('weapon', name, owner, weight, durability)
        self.__damage = damage

    def damage(self):
        return self.__damage

    def use(self, target: Character):
        target.damage(self.__damage)
        self.__durability -= 1
        if self.__durability > 0:
            self.__durability -= 1
            print(f'{self.__name} was used by {self.__owner}')
        else:
            print(f'{self.__name} is broken')

    def __str__(self):
        return f'{super().__str__()} - {self.damage()} damage'