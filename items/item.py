from lore import lore_text
class Item():
    VALID_ITEM_TYPES = ['weapon', 'consumable']

    def __init__(self, category, name, owner, weight: int, durability: int):
        if category not in self.VALID_ITEM_TYPES:
            raise ValueError("Invalid item type")
        self.__name = name
        self.__category = category
        self.__owner = owner
        self.__weight = weight
        self.__durability = durability

    def category(self):
        return self.__category
    
    def name(self):
        return self.__name

    def owner(self):
        return self.__owner
    
    def weight(self):
        return self.__weight
    
    def durability(self):
        return self.__durability
    
    def use(self):
        from characters.player import Player
        if isinstance(self.__owner, Player):
            if self.__durability > 0:
                self.__durability -= 1
                if self.__durability == 0:
                    lore_text(F'{self.__name} was used and is now broken')
                    print('')
                    self.__owner.remove_item(self)
            else:
                lore_text(f'{self.__name} is broken')
                print('')
                self.__owner.remove_item(self)
    
    def __str__(self):
        return f'{self.__name} - Owned by {self.__owner}, Item type: {self.__category}, Weight: {self.__weight}, Durability: {self.__durability}'