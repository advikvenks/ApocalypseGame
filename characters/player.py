import entityCreator
from items.consumable import Consumable
from items.item import Item
from items.weapon import Weapon
from .character import Character

class Player(Character):
    def __init__(self, name, gender, inventory, health):
        super().__init__('player', health)
        self.__name = name
        self.__gender = gender
        self.__inventory = [[],[]]
        for item in inventory:
            if isinstance(item, list):
                item = entityCreator.createEntity('item', *item)
                if item is not None and isinstance(item, Item):
                    category = item.category()
                    if category == 'weapon':
                        self.__inventory[0].append(item)
                    elif category == 'consumable':
                        self.__inventory[1].append(item)
                else:
                    print("Invalid item")
            elif isinstance(item, Weapon):
                self.__inventory[0].append(item)
            elif isinstance(item, Consumable):
                self.__inventory[1].append(item)
            else:
                print("Invalid item type")
                
    def name(self):
        return self.__name
    
    def gender(self):
        return self.__gender
    
    def inventory(self):
        return self.__inventory
    
    def add_or_remove_item(self, item, action):
        if isinstance(item, list):
            item = entityCreator.createEntity('item', *item)
        
        if item is not None and isinstance(item, Item):
            if  action == 'add':
                category = item.category()
                if category == 'weapon':
                    self.__inventory[0].append(item)
                elif category == 'consumable':
                    self.__inventory[1].append(item)
            if action == 'remove':
                category = item.category()
                if category == 'weapon':
                    self.__inventory[0].remove(item)
                elif category == 'consumable':
                    self.__inventory[1].remove(item)
        else:
            print("Invalid item")

    def add_item(self, item):
        self.add_or_remove_item(item, 'add')
    
    def remove_item(self, item):
        self.add_or_remove_item(item, 'remove')
    
    def __str__(self):
        names_inventory = []

        for sublist in self.__inventory:
            names_sublist = []
            for item in sublist:
                if isinstance(item, Item):
                    names_sublist.append(item.name())
            names_inventory.append(names_sublist)

        return f'{self.__name} - Health: {super().health()}, Gender: {self.__gender}, Inventory: {names_inventory}'