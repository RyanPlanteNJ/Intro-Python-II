from room import Room
from player import Player
from weapons import Weapons
from equipment import Equipment
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
    'torch': Item('Torch', 'Not very useful, but it will do for now. Maybe we will find something better on your way through this place', 'E'),

    'dagger': Weapons("Rasaka's Fang", 'A dagger made of Rasaka’s poisoned fang, still dripping with its poison.\n\nYou may keep this item in your inventory.\nYou may sell this item in the shop.\n','C', 'Dagger', "\nAttack Power +25\n\nInflicts ‘Paralysis’ and ‘Bleeding’ on attack.\n\n‘Paralysis’: The target has a chance to become immobilized.\n‘Bleeding’: The target will lose [1%] health per second.\n\n"),

    'helmet': Equipment('Red Knights Helmet', 'As weird as it is, when you wear this helmet, it gives you more strength\n', 'S', 'Helmet', "\nPhysical Damage Reduction +15%\nStrength +20\nStamina +20")
}

room['foyer'].add_item(item['torch'])
room['overlook'].add_item(item['dagger'])
room['treasure'].add_item(item['helmet'])

options = "Options:[Options]\nInventory:[View]\nItem:[Take][Drop][Equip][Unequip]\nDirections:[N][S][E][W]\nSystem:[Quit] to Quit\n"

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
    user_input = input('\nEnter [Play] to become a Player or [Quit] to Quit >>>').lower().strip()
    if user_input == "play":
        name = input('\nWhat is your name Player?').upper().strip()
        if name !='':
            player.name = name
            print(f"\nWelcome, Player {player.name}:\nYou're current location is the {player.current_room}\n\n{options}")
    elif user_input == 'quit':
        second_input = input("\nIf you refuse, you will die from your wounds. Are you sure you don't want to become a Player >>>").lower().strip()
        if second_input == 'play':
            name = input('\nWhat is your name Player? >>>').upper().strip()
            if name !='':
                player.name = name
                print(f"\nWelcome, Player {player.name}:\nYou're current location is {player.current_room}\n\n{options}")
        elif second_input == 'quit':
            print('You have died from your wounds')


    while user_input == 'play' or second_input == 'play':
        print('============================================================')
        choice = input('Please choose an option:\n').lower().strip()
        if len(choice.split()) == 2:
            handle_item = choice.split()
            # print(handle_item)
            if handle_item[0] == 'take':
                try:
                    selected_item = item[handle_item[1].lower()]
                    if selected_item in player.current_room.items:
                        player.take_item(selected_item)
                        player.current_room.remove_item(selected_item)
                        print(f'You decided to grab {selected_item.name}\n')
                        print('\nInventory:\n')
                        for inventory_item in player.inventory:
                            print(f'{inventory_item.name}\n\n')
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
            elif handle_item[0] == 'equip':
                try:
                    selected_item = item[handle_item[1].lower()]
                    if selected_item in player.inventory:
                        player.equip_item(selected_item)
                        player.drop_item(selected_item)
                        print(f'\nYou equipped {selected_item.name}')
                    else:
                        print('\nThis item does not exist in your inventory')
                except:
                    print('\nThis item does not exist in your inventory')
            elif handle_item[0] == 'unequip':
                try:
                    selected_item = item[handle_item[1].lower()]
                    if selected_item in player.equipped:
                        player.take_item(selected_item)
                        player.unequip_item(selected_item)
                        print(f'\nYou just unequipped {selected_item.name}')
                    else:
                        print('\nThis item is not equipped to you currently')
                except:
                    print('\nThis item is not equipped to you currently')
        elif choice in directions:
            if hasattr(player.current_room,f'{choice}_to'):
                player.current_room = getattr(
                player.current_room, f'{choice}_to'
                )
                print(f'\n{player.current_room}\n')
                print(f'\n{options}')
            else:
                print('Cannot move in that direction')
        elif choice == 'view':
            print('\nInventory:\n')
            for inventory_item in player.inventory:
                print(f'\n{inventory_item}\n\n')
                print('=====================================================')
            print('Equipped Items: \n')
            for equipped_item in player.equipped:
                print(f'{equipped_item.name}\n\n')
        elif choice == "options":
            print(f'\n{options}')
        elif choice == 'quit':
            print(f'\nThanks for playing {player.name}')
            sys.exit()
        else:
            print('Invalid command')
        print('============================================================')
        print('Items\n')
        for room_item in player.current_room.items:
            print(room_item)

solo_leveling()
