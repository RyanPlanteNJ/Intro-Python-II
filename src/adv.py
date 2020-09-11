from room import Room
from player import Player
from item import Item
import sys


# Declare all the rooms
room = {
    'outside_start': Room("Dark Cave", "You awake in an unknown place. Unaware of your surroundings, you begin to look around for any clues"),

    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east"),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow': Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.")
}

# Link rooms together
room['outside_start'].n_to = room['outside']
room['outside'].s_to = room['outside_start']
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

item = {
    'torch': Item('Torch', 'Not very useful, but it will do for now. Maybe we will find something better on your way through this place'),
    'dagger': Item("Rasaka's Fang",'You feel it eminating immense power'),
    'helmet': Item('Red Knights Helmet', 'As weird as it is, when you wear this helmet, it gives you more strength ')
}

room['foyer'].add_item(item['torch'])
room['overlook'].add_item(item['dagger'])
room['treasure'].add_item(item['helmet'])



options = "Options:\nInventory:[View]\nItem:[Take][Drop]\nDirections:[N][S][E][W]\nSystem:[Q] to Quit\n"

directions = {'n','s','e','w'}

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def solo_leveling():
    name = "Solo Leveling"
    player = Player(name, room['outside_start'])
    print('\nYou have completed all the necessary requirements. You have earned the right to become a Player. Will you accept?')
    user_input = input('\nEnter [P] to become a Player or [Q] to Quit >>>').lower().strip()

    if user_input == "p":
        name = input('\nWhat is your name Player?').upper().strip()
        if name !='':
            player.name = name
        print(f"\nWelcome, Player {player.name}:\n You're current location is {player.current_room.name}\n{options}")
    elif user_input != 'p':
        second_input = input("\nIf you refuse, you will die from your wounds. Are you sure you don't want to become a Player >>>").lower().strip()
        if second_input == 'p':
            name = input('\nWhat is your name Player? >>>').upper().strip()
            if name !='':
                player.name = name
                print(f"\nWelcome, Player {player.name}:\n You're current location is {player.current_room}")
        elif second_input != 'p':
            print("You have died from your wounds")


    while user_input == 'p' or second_input == 'p':
        print('============================================================')
        choice = input('Please choose an option:\n').lower().strip()
        print(f'{options}')
        if len(choice.split()) == 2:
            handle_item = choice.split()
            # print(handle_item)
            if handle_item[0] == 'take':
                try:
                    selected_item = item[handle_item[1].lower()]
                    if selected_item in player.current_room.items:
                        player.take_item(selected_item)
                        player.current_room.remove_item(selected_item)
                    else:
                        print('This item does not exist')
                except:
                    print('This item does not exist')
            elif handle_item[0] == 'drop':
                try:
                    selected_item = item[handle_item[1].lower()]
                    if selected_item in player.inventory:
                        player.current_room.add_item(selected_item)
                        player.drop_item(selected_item)
                        print(f'You dropped {selected_item.name}')
                    else:
                        print('This item does not exist in your inventory')
                except:
                    print('This item does note exist in your invenotry')
        elif choice in directions:
            if hasattr(player.current_room,f'{choice}_to'):
                print(f'Moving {choice} from your current location')
                player.current_room = getattr(
                player.current_room, f'{choice}_to'
                )
                print(f'\n{player.current_room}\n')
                print(f'\n{options}')
            else:
                print('Cannot move in that direction')
        elif choice == 'view':
            print('Inventory: \n')
            for inventory_item in player.inventory:
                print(f'{inventory_item}\n')
        elif choice == 'q':
            print(f'\nThanks for playing {player.name}')
            sys.exit()
        else:
            print('Invalid command')
        print('============================================================')
        print('Items\n')
        for room_item in player.current_room.items:
            print(room_item)

solo_leveling()
