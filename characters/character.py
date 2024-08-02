class Character():
    VALID_CHARACTER_TYPES = ['player', 'neighbour', 'zombie']

    def __init__(self, type, health):
        if type not in self.VALID_CHARACTER_TYPES:
            raise ValueError("Invalid character type")
        self.__type = type
        self.__health = health

    def typeof(self):
        return self.__type
    
    def damage(self, damage):
        self.__health -= damage

    def heal(self, healAmount):
        self.__health += healAmount
    
    def health(self):
        return self.__health