from items.consumable import Consumable
from items.item import Item
from items.weapon import Weapon
from .character import Character
from items.itemHandler import ItemHandler

class Player(Character):
    def __init__(self, name, gender, inventory, health):
        super().__init__('player', health)
        self.__name = name
        self.__gender = gender
        self.__inventory = [[],[]]
        for item in inventory:
            if isinstance(item, list):
                item = ItemHandler.create_item(*item)
                if item is not None:
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
    
    def add_item(self, item):
        if isinstance(item, list):
            item = ItemHandler.create_item(*item)
            if item is not None:
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
    
    def remove_item(self, item):
        if isinstance(item, list):
            item = ItemHandler.create_item(*item)
            if item is not None:
                category = item.category()
                if category == 'weapon':
                    self.__inventory[0].remove(item)
                elif category == 'consumable':
                    self.__inventory[1].remove(item)
            else:
                print("Invalid item")
        elif isinstance(item, Weapon):
            self.__inventory[0].remove(item)
        elif isinstance(item, Consumable):
            self.__inventory[1].remove(item)
        else:
            print("Invalid item type")
    
    def use_weapon(self, weapon: Weapon, target: Character):
        if weapon in self.__inventory[0]:
            weapon.use(target)
    
    def __str__(self):
        names_inventory = []

        for sublist in self.__inventory:
            names_sublist = []
            for item in sublist:
                if isinstance(item, Item):
                    names_sublist.append(item.name())
            names_inventory.append(names_sublist)

        return f'{self.__name} - Health: {super().health()}, Gender: {self.__gender}, Inventory: {names_inventory}'