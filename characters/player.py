from .character import Character
from items.itemHandler import ItemHandler

class Player(Character):
    def __init__(self, name, gender, inventory, health):
        super().__init__('player', health)
        self.__name = name
        self.__gender = gender
        self.__inventory = [[],[]]
        for item_list in inventory:
            if item_list != []:
                if type(item_list) == type([]):
                    item = ItemHandler.create_item(item_list)
                    if item.category() == 'weapon':
                        self.__inventory[0].append(item)
                    elif item.category() == 'consumable':
                        self.__inventory[1].append(item)

    def name(self):
        return self.__name
    
    def gender(self):
        return self.__gender
    
    def add_item(self, item):
        if type(item) == type([]):
                item = ItemHandler.create_item(item)
                if item.category() == 'weapon':
                    self.__inventory[0].append(item)
                elif item.category() == 'consumable':
                    self.__inventory[1].append(item)
        else:
            if item.category() == 'weapon':
                self.__inventory[0].append(item)
            elif item.category() == 'consumable':
                self.__inventory[1].append(item)
    
    def remove_item(self, item):
        if type(item) == type([]):
                item = ItemHandler.create_item(item)
                if item.category() == 'weapon':
                    self.__inventory[0].remove(item)
                elif item.category() == 'consumable':
                    self.__inventory[1].remove(item)
        else:
            if item.category() == 'weapon':
                self.__inventory[0].remove(item)
            elif item.category() == 'consumable':
                self.__inventory[1].remove(item)
    
    def use_weapon(self, weapon, target):
        if weapon in self.__inventory[0]:
            weapon.use(target)
    
    def __str__(self):
        return f'{self.__name} - Health: {super().health()}, Gender: {self.__gender}, Inventory: {self.__inventory}'