from player import Player
from room import Room

class Game(Player):
    def __init__(self, player_items=[], room_items=[]):
        super().__init__(player_items)

    def handle_items(self, tools):
        choose = input(
            f"You happen to see items around the room you are in. [0] to leave them, [1] to look closer, [2] to drop items you currently have: ")
        if choose == str(1):
            picked = input(f'Pick which items you want to carry: {tools} >>>')
            try:
                self.player_add(tools[int(picked)-1])
                self.room_drop(int(picked)-1)
            except IndexError:
                print('This item does not exist. ')
                pass
        elif choose == str(2):
            try:
                if len(self.player_items) == 0:
                    print('You have no items in your possession')
                else:
                    drop = input(f'Which item from your storage do you want to drop: {self.player_items} >>>')
                    self.player_drop(int(drop)-1)
                    self.room_add(tools[int(drop)-1])
            except IndexError:
                pass
        if len(self.player_items) > 0:
            print(f'Current Storage: {self.player_items} \n')
        else:
            print('You have nothing in your storage that you can use')

    def control_direction(self):
        return input('Pick a direction [n,s,e,w]: ')
