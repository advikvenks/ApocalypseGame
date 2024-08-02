from .weapon import Weapon
from .consumable import Consumable

class ItemHandler:
    def create_item(category, name, owner, weight, durability, **kwargs) :
        if category == 'weapon':
            return Weapon(name, owner, weight, durability, kwargs['damage'])
        elif category == 'consumable':
            return Consumable(name, owner, weight, durability, kwargs['heal'])