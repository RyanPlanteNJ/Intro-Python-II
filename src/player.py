# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player(Item):
    def __init__(self, current_room, player_items=[]):
        super().__init__(player_items)
        self.current_room = current_room

    def __str__(self):
        return f'{self.items}'

    def stuff(self):
        output = ''
        n = 1
        for tools in self.player_items:
            output += f'\n{n}.{tools}'
            n+=1
        return output +'\n>>>'
