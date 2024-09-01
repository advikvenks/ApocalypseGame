from .character import Character

class Zombie(Character):
    def __init__(self, health, damage):
        super().__init__('zombie', health)
        self.__damage = damage
    
    def damageAmount(self):
        return self.__damage
    
    def attack(self, player):
        player.damage(self.__damage)
    
    def __str__(self):
        return f'Health: {super().health()}, Damage: {self.__damage}'