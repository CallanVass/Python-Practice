class Character:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.copper = 0
        self.inv = Inventory([], 0, 0, 0)

    
class Chest:
    def __init__(self, items, gold, silver, copper):
        self.inv = Inventory(items, gold, silver, copper)

class Inventory:
    def __init__(self, items, gold, silver, copper):
        self.items = items
        self.gold = gold
        self.silver = silver
        self.copper = copper

    #Setter
    def set_currency(self, gold, silver, copper):
        self.copper = gold * 10000 + silver * 100 + copper

    #Getter
    def get_currency(self):
        gold = self.copper // 10000
        silver = (self.copper % 10000) // 100
        copper = self.copper % 100
        return gold, silver, copper
