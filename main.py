from items.itemHandler import ItemHandler
from characters.characterHandler import CharacterHandler

def main():
    sword = ItemHandler.create_item('weapon', 'sword', 'player', 10, 100, damage=80)
    bow = ItemHandler.create_item('weapon', 'bow', 'player', 10, 100, damage=50)
    cake = ItemHandler.create_item('consumable', 'cake', 'player', 10, 1, heal=30)
    player = CharacterHandler.create_character('player', 100, name='casu martzu', gender='autogender', inventory=[sword, bow, cake])
    print(player)

if __name__ == '__main__':
    main()