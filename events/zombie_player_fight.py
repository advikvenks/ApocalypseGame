import time
from characters.player import Player
from characters.zombie import Zombie
from items.consumable import Consumable
from items.weapon import Weapon
from lore import zombie_vs_player, lore_text
import random

def AttemptRun(player: Player, zombie: Zombie):
    healthDifference = (player.health() - (zombie.damageAmount() * 2)) / 100
    if healthDifference > 0:
        probability = 0.1 + healthDifference * (0.9)

        probability = min(1.0, max(0.1, 0.1 + healthDifference * 0.9))

        lore_text(zombie_vs_player['playerRun'])
        time.sleep(1 - healthDifference)
        print('\n')

        if random.random() > probability:
            lore_text(zombie_vs_player['playerRunFail'])
        else:
            lore_text(zombie_vs_player['playerRunSuccess'])

def FightLoop(player: Player, zombie: Zombie):
    while True:
        print('\n')
        lore_text(zombie_vs_player['start'])
        print('\n')
        lore_text(zombie_vs_player['initialOptions'])
        print('\n')
        initialChoice = input()
        if initialChoice == '1':
            while True:
                PlayerTurn(player, zombie)
                if zombie.health() <= 0:
                    return 'zombie_dead'
        
                ZombieTurn(player, zombie)
                if player.health() <= 0:
                    return 'dead'
                
                lore_text(zombie_vs_player['continue'])
                lore_text(zombie_vs_player['continueOptions'])
                choice = input()
                if choice == '2':
                    AttemptRun(player, zombie)
                    break

        elif initialChoice == '2':
            AttemptRun(player, zombie)
            break
        else:
            print('Please choose either 1 or 2.')
    

def PlayerTurn(player: Player, zombie: Zombie):
    while True:
        try:
            print('\n')
            lore_text(zombie_vs_player['playerFight'])
            print('\n')
            lore_text(zombie_vs_player['fightOptions'])
            print('\n')
            choice = int(input())
            item_names = []
            if choice == 1:
                lore_text('You choose to attack. What weapon do you use?')
                print('\n')
                for index, item in enumerate(player.inventory()[0]):
                    if isinstance(item, Weapon):
                        lore_text(f'\n{item.name()}[{index + 1}]')
                        item_names.append(item.name())
                print('\n')
                choice = int(input())
                weapon = player.inventory()[0][choice - 1]
                if isinstance(weapon, Weapon):
                    if isinstance(zombie, Zombie):
                        weapon.use(zombie)
                        if zombie.health() <= 0:
                            return
                        else: 
                            lore_text(f'You used {item_names[choice - 1]} on the zombie. It dealt {weapon.damage()} damage and the zombie has {zombie.health()} health left.')
                            break
            elif choice == 2:
                lore_text('You choose to heal. What consumable do you use?')
                print('\n')
                for index, item in enumerate(player.inventory()[1]):
                    if isinstance(item, Consumable):
                        lore_text(f'\n{item.name()}[{index + 1}]')
                        item_names.append(item.name())
                print('\n')
                try:
                    choice = int(input())
                    consumable = player.inventory()[1][choice - 1]
                    if isinstance(consumable, Consumable):
                        if isinstance(player, Player):
                            player.heal(consumable.healAmount())
                            if player.health() >= 100:
                                player.setHealth(100)
                            lore_text(f'You used {item_names[choice - 1]} on yourself. It healed {consumable.healAmount()} health and you now have {player.health()} health.')
                            break
                except:
                    lore_text('Invalid choice', 0.05)
            else:
                lore_text('Invalid choice', 0.05)
        except:
            lore_text('Invalid choice', 0.05)

def ZombieTurn(player: Player, zombie: Zombie):
    print('\n')
    if random.randint(1,5) != 1:
        zombie.attack(player)
        if player.health() <= 0:
            return
        else:
            lore_text(f'The zombie attacked you and you took {zombie.damageAmount()} damage. You have {player.health()} health remaining')
    else:
        lore_text('The zombie missed you.')
        

def ZombieVsPlayer(player: Player, zombie: Zombie):
    result = FightLoop(player, zombie)
    if result == 'dead':
        lore_text('You died.', 0.05)
    else:
        lore_text(f'You killed the zombie and have {player.health()} health remaining.')