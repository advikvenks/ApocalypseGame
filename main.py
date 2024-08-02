from items.itemHandler import ItemHandler
from characters.characterHandler import CharacterHandler

def main():
    sword = CharacterHandler.create_character('zombie', 100, damage=20)
    print(sword)

if __name__ == '__main__':
    main()