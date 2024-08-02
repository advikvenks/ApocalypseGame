class Item():
    VALID_ITEM_TYPES = ['weapon', 'consumable']

    def __init__(self, category, name, owner, weight, durability):
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
        if self.__durability > 0:
            self.__durability -= 1
            print(f'{self.__name} was used by {self.__owner}')
        else:
            print(f'{self.__name} is broken')
    
    def __str__(self):
        return f'{self.__name} - Owned by {self.__owner}, Item type: {self.__category}, Weight: {self.__weight}, Durability: {self.__durability}'