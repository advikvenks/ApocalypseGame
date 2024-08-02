from .player import Player
from .zombie import Zombie

class CharacterHandler():
    @staticmethod
    def create_character(category, health, **kwargs):
        if category == 'player':
            return Player(kwargs['name'], kwargs['gender'], kwargs['inventory'], health)
        elif category == 'zombie':
            return Zombie(health, kwargs['damage'])