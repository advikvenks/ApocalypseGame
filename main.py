from characters.player import Player
from characters.zombie import Zombie
from items.itemHandler import ItemHandler
from characters.characterHandler import CharacterHandler
from events.zombie_player_fight import ZombieVsPlayer

def main():
    player = CharacterHandler.create_character('player', 100, name='casu martzu', gender='gender', inventory=[])
    sword = ItemHandler.create_item('weapon', 'Sword', player, 10, 100, damage=20)
    bow = ItemHandler.create_item('weapon', 'Bow', player, 10, 1, damage=40)
    cake = ItemHandler.create_item('consumable', 'Cake', player, 10, 1, heal=50)
    if isinstance(player, Player):
        player.add_item(sword)
        player.add_item(bow)
        player.add_item(cake)
    zombie = CharacterHandler.create_character('zombie', 100, damage=30)
    if isinstance(player, Player) and isinstance(zombie, Zombie):
        ZombieVsPlayer(player, zombie)
    

if __name__ == '__main__':
    main()