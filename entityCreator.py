from characters.player import Player
from characters.zombie import Zombie
from items.weapon import Weapon
from items.consumable import Consumable
from lore import lore_text

def createEntity(entityType, **kwargs):
    if entityType == 'item':
        if kwargs['category'] == 'weapon':
            return Weapon(kwargs['name'], kwargs['owner'], kwargs['weight'], kwargs['durability'], int(kwargs['damage']))
        elif kwargs['category'] == 'consumable':
            return Consumable(kwargs['name'], kwargs['owner'], kwargs['weight'], kwargs['durability'], int(kwargs['heal']))
    elif entityType == 'character':
        if kwargs['category'] == 'player':
            return Player(kwargs['name'], kwargs['gender'], kwargs['inventory'], kwargs['health'])
        elif kwargs['category'] == 'zombie':
            return Zombie(kwargs['health'], kwargs['damage'])

def entityCreateText(entityType, **kwargs):
    lore_text('')