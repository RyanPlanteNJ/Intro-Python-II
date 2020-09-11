class Item:
    def __init__(self, room_items=[], player_items=[], items=[]):
        self.player_items = player_items
        self.room_items = room_items
        self.items = items

    def player_add(self, item):
        self.player_items.append(item)

    def player_drop(self, item):
        self.player_items.pop(item)

    def room_add(self, item):
        self.room_items.append(item)

    def room_drop(self, item):
        self.room_items.pop(item)
