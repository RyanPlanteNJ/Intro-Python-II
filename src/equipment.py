from item import Item

class Equipment(Item):
    def __init__(self, name, description, rarity, equipment_type, status_effects):
        super().__init__(name, description, rarity)
        self.equipment_type = equipment_type
        self.status_effects = status_effects

    def __str__(self):
        return f'{super().__str__()}Rarity: {self.rarity}\nType: {self.equipment_type}\nStatus Effects: {self.status_effects}'
