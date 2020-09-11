# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room, equipped = None, inventory = None):
        self.name = name
        self.current_room = current_room
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        if equipped is None:
            self.equipped = []
        else:
            self.equipped = equipped

    def equip_item(self, item):
        self.equipped.append(item)

    def unequip_item(self, item):
        self.equipped.remove(item)

    def take_item(self, item):
        self.inventory.append(item)


    def drop_item(self, item):
        self.inventory.remove(item)
