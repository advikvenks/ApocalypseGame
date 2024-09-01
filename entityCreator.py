from characters.zombie import Zombie
from items.weapon import Weapon
from items.consumable import Consumable
from lore import lore_text, entity_creation

def createEntity(entityType, **kwargs):
    if entityType == 'item':
        if kwargs['category'] == 'weapon':
            return Weapon(kwargs['name'], kwargs['owner'], kwargs['weight'], kwargs['durability'], int(kwargs['damage']))
        elif kwargs['category'] == 'consumable':
            return Consumable(kwargs['name'], kwargs['owner'], kwargs['weight'], kwargs['durability'], int(kwargs['heal']))
    elif entityType == 'character':
        if kwargs['category'] == 'player':
            from characters.player import Player
            return Player(kwargs['name'], kwargs['gender'], kwargs['inventory'], kwargs['health'])
        elif kwargs['category'] == 'zombie':
            return Zombie(kwargs['health'], kwargs['damage'])

def entityCreateText(skip = ''):
    if skip == 'player':
        while True:
            try:
                lore_text('Enter your name: ')
                name = input()
                lore_text('Enter your gender: ')
                gender = input()
                return createEntity('character', category='player', name=name, gender=gender, inventory=[], health=100)
            except:
                lore_text('Invalid input. Please try again.')
    else:
        lore_text(entity_creation['entityType'] + '\n')
        while True:
            try:
                lore_text('Character[1]\nWeapon[2]\n')
                choice = int(input())
                if choice == 1:
                    lore_text(entity_creation['characterType'] + '\n')
                    lore_text('Player[1]\nZombie[2]\n')
                    choice2 = int(input())
                    if choice2 == 1:
                        lore_text('Enter the player\'s name: ')
                        name = input()
                        lore_text('Enter the player\'s gender: ')
                        gender = input()
                        return createEntity('character', category='player', name=name, gender=gender, inventory=[], health=100)
                    elif choice2 == 2:
                        lore_text('Enter the zombie\'s damage: ')
                        damage = int(input())
                        return createEntity('character', category='zombie', health=100, damage=damage)
                elif choice == 2:
                    lore_text(entity_creation['itemType'] + '\n')
                    lore_text('Weapon[1]\nConsumable[2]\n')
                    choice2 = int(input())
                    if choice2 == 1:
                        lore_text('Enter the weapon\'s name: ')
                        name = input()
                        lore_text('Enter the weapon\'s owner: ')
                        owner = input()
                        lore_text('Enter the weapon\'s weight: ')
                        weight = int(input())
                        lore_text('Enter the weapon\'s durability: ')
                        durability = int(input())
                        lore_text('Enter the weapon\'s damage: ')
                        damage = int(input())
                        return createEntity('item', category='weapon', name=name, owner=owner, weight=weight, durability=durability, damage=damage)
                    elif choice2 == 2:
                        lore_text('Enter the consumable\'s name: ')
                        name = input()
                        lore_text('Enter the consumable\'s owner: ')
                        owner = input()
                        lore_text('Enter the consumable\'s weight: ')
                        weight = int(input())
                        lore_text('Enter the consumable\'s durability: ')
                        durability = int(input())
                        lore_text('Enter the consumable\'s heal amount: ')
                        heal = int(input())
                        return createEntity('item', category='consumable', name=name, owner=owner, weight=weight, durability=durability, heal=heal)
                else:
                    print('Invalid choice. Try again')
            except:
                lore_text('Invalid input. Try again')