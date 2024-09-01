from characters.player import Player
from characters.zombie import Zombie
import entityCreator
from events.zombie_player_fight import ZombieVsPlayer

def main():
    player = entityCreator.entityCreateText('player')
    print(player)
    sword = entityCreator.createEntity('item', category='weapon', name='Sword', owner=player, weight=10, durability=100, damage=20)
    bow = entityCreator.createEntity('item', category='weapon', name='Bow', owner=player, weight=10, durability=1, damage=40)
    cake = entityCreator.createEntity('item', category='consumable', name='Cake', owner=player, weight=10, durability=1, heal=50)
    if isinstance(player, Player):
        player.add_item(sword)
        player.add_item(bow)
        player.add_item(cake)
    zombie = entityCreator.createEntity('character', category='zombie', health=100, damage=30)
    if isinstance(player, Player) and isinstance(zombie, Zombie):
        ZombieVsPlayer(player, zombie)
    

if __name__ == '__main__':
    main()