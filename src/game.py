from player import Player
from room import Room

class Game(Player):
    def __init__(self, player_items=[], room_items=[]):
        super().__init__(player_items, room_items)

    def handle_items(self, tools):
        choose = input(
            "You happen to see items around the room you are in. [Continue forward] to leave them, [investigate] to look closer, [look in bag] to see what items you are currently holding, [remove items] to drop items you currently have: ")
        if choose == 'investigate':
            picked = input(f'Pick which items you want to carry: {tools} >>>')
            try:
                self.player_add(tools[int(picked)-1])
            except IndexError:
                print('This item does not exist.')
                pass
        elif choose == 'remove items':
            try:
                if len(self.player_items) == 0:
                    print('You have no items in your possession')
                else:
                    drop = input(f'Which item from your storage do you want to drop : {self.player_items} >>>')
                    self.player_drop(int(drop)-1)
            except IndexError:
                pass
        elif choose == 'look in bag':
            try:
                if len(self.player_items) == 0:
                    print('There are no items in your storage')
                else:
                    print(f'Current storage: {self.player_items}\n')
            except IndexError:
                pass
        if len(self.player_items) > 0:
            print(f'\nCurrent storage: {self.player_items}\n')
        else:
            print('You might want to grab some stuff')
    def control_direction(self):
        return input('Pick a direction [n,s,e,w]: ')

        #paresstr = input().split(" ")
        #     if parsestr[1]
