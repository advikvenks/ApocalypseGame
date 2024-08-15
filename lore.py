import time
from characters.player import Player


def lore_text(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

zombie_vs_player = {'start':'You encounter a zombie. What would you like to do?',
                    'initialOptions': 'Fight[1]\nRun[2]',
                    'playerFight':'You choose to fight. What do you want to do now?',
                    'fightOptions':'Attack[1]\nHeal[2]',
                    'playerRun':'You choose to run. Good luck.',
                    'playerRunFail':'You were too weak to run away and were caught by the zombie.',
                    'playerRunSuccess':'You successfully escaped the zombie.'}