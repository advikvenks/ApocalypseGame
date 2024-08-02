import weapon

class ItemHandler:
    
    def create_item(self, category, name, owner, weight, durability, *args) :
        if category == 'weapon':
            return weapon.Weapon(category, name, owner, durability, args[0])