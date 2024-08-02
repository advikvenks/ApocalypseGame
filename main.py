from items.itemHandler import ItemHandler

def main():
    sword = ItemHandler.create_item('weapon', name='sword', owner='me', weight='10', durability='100/100', damage='100')
    print(sword)

if __name__ == '__main__':
    main()