# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room(Item):
    def __init__(self, name, description, room_items=[]):
        super().__init__(room_items)
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        room = f'{self.name}: {self.description}\n'
        items = f'{self.room_items}'
        if self.n_to:
            return f'{room} \n You have entered the {self.name} from the {self.n_to.name} \n'
        elif self.s_to:
            return f'{room} \n You have entered the {self.name} from the {self.s_to.name} \n'
        elif self.e_to:
            return f'{room} \n You have entered the {self.name} from the {self.e_to.name} \n'
        elif self.w_to:
            return f'{room} \n You have entered the {self.name} from the {self.w_to.namme} \n'
        return room + items

    def stuff(self):
        output = ''
        n = 1
        for tools in self.room_items:
            output += f'\n{n}.{tools}'
            n+=1
        return output +'\n>>>'
