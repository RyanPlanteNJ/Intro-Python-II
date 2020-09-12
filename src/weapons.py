from item import Item

class Weapons(Item):
    def __init__(self, name, description, rarity, weapon_type, status_effects):
        super().__init__(name, description, rarity)
        self.weapon_type = weapon_type
        self.status_effects = status_effects

    def __str__(self):
        return f'{super().__str__()}Type: {self.weapon_type}\n\nStatus Effects: {self.status_effects}'
