# Sam Reyes
# Text based game

#print a main menu and commands
def show_instructions():
    print("Demons Lair")
    print("Collect the 6 items to defeat the Demon King and win the game!")
    print("Move commands: go north, go south, go east, go west")
    print("Add to Inventory: get 'item name'")
    print("To exit the game: 'Exit'")
    print("Start at the Graveyard")

#A dictionary linking rooms to another room
def Main():
    rooms = {
        'Graveyard': {'east': 'Hall'},
        'Hall': {'north': 'Study', 'south': 'Armory', 'east': 'Kitchen', 'west': 'Graveyard', 'item': 'map'},
        'Study': {'east': 'Bedroom', 'south': 'Hall', 'item': 'sword'},
        'Bedroom': {'west': 'Study', 'item': 'key'},
        'Kitchen': {'north': 'Garage', 'west': 'Hall', 'item': 'health-kit'},
        'Garage': {'south': 'Kitchen', 'item': 'cloak'},
        'Armory': {'north': 'Hall', 'east': 'Secret Room', 'item': 'armor'},
        'Secret Room': {'west': 'Armory', 'item': 'Demon King'}}

    players_move = ['north', 'south', 'east', 'west']
    current_room = 'Graveyard'
    inventory = []
    show_instructions()

    while True:
        if current_room == 'Secret Room':
            if len(inventory) == 6:
                print('The Demon King bleeds...')
                print('YOU SAVED THE WORLD! YOU WIN!')
                print('Thanks for playing!')
                break
            else:
                print('The Demon King took your soul...')
                print('not enough items to save yourself...')
                print('YOU DIED... GAME OVER!')
                break

        #display current location
        print()
        print('You are in the {}.'.format(current_room))
        print('Inventory:', inventory)
        room_dict = rooms[current_room]

        if "item" in room_dict:
            item = room_dict["item"]
            if item not in inventory:
                print("You see a", item)

        #get user input
        command = input("What do you do? ").split()
        #movement
        if command[0] == 'go':
            if command[1] in players_move:
                room_dict = rooms[current_room]
                if command[1] in room_dict:
                    current_room = room_dict[command[1]]
                else:
                    print('You cannot go that way')
            else:
                print('Invalid entry')
        # quit
        elif command[0] in ['exit', 'quit']:
            print('Thanks for playing!')
            break
        # get item
        elif command[0] == 'get':
            if command[1] == item:
                inventory.append(item)
                print(item, "collected")
            else:
                print('Invalid command')
        #bad command
        else:
            print('Invalid input')

Main()
