from .weapon import Weapon
from .consumable import Consumable

class ItemHandler:
    @staticmethod
    def create_item(category, name, owner, weight: int, durability: int, **kwargs) :
        if category == 'weapon':
            return Weapon(name, owner, weight, durability, int(kwargs['damage']))
        elif category == 'consumable':
            return Consumable(name, owner, weight, durability, int(kwargs['heal']))