import random

# Core game functions

def exposition():

    # Returns (does not print) a message to be displayed at the start of the game.
   
    expo_text = "You find yourself lost in a dimly lit tomb.\n" \
                "Its builders are unknown to the modern world.\n" \
                "Your gut tells you there's treasure nearby.\n"
    return expo_text

def create_world():

    # Creates and returns a world object in its initial state.

    world = {"status"    :
                "playing",
            "player"    : {
                "location"  : "rm_start",
                "inventory" : []},
            "world_map"       : [
                {"location"     : "rm_start",
                 "about"        : "You are in the central room. Light filters \n"
                                  "in through the ceiling. You see four doors, \n"
                                  "one in each direction. Which do you take?",
                 "neighbors"    : ["rm_gold", "rm_map", "rm_dark", "rm_torch"],
                 "loot"         : []},

                {"location"     : "rm_gold",
                 "about"        : "You find the gold! \n"
                                  "You hear a soft noise in the room to the west.",
                 "neighbors"    : ["", "rm_start", "", "death1"],
                 "loot"         : ["GOLD"]},

                {"location"     : "rm_map",
                 "about"        : "You find a dusty old map. This should help.",
                 "neighbors"    : ["rm_start", "", "death2", "rm_key"],
                 "loot"         : ["MAP"]},

                {"location"     : "rm_lit",
                 "about"        : "Your trusty torch lights the way. \n"
                                  "To the north you see a staircase. \n"
                                  "To the south you see a bottomless pit.",
                 "neighbors"    : ["rm_exit", "death2", "", "rm_start"],
                 "loot"         : []},
                
                {"location"     : "rm_dark",
                 "about"        : "You can't see a thing. \n"
                                  "Do you risk fumbling around in the dark, or \n"
                                  "do you play it safe and turn back?",
                 "neighbors"    : ["rm_exit", "death2", "", "rm_start"],
                 "loot"         : []},

                {"location"     : "rm_torch",
                 "about"        : "You find a lit torch. \n"
                                  "You decide it's better not to question \n"
                                  "why it hasn't burnt out after all this time.",
                 "neighbors"    : ["death1", "rm_key", "rm_start", ""],
                 "loot"         : ["TORCH"]},
                
                {"location"     : "rm_key",
                 "about"        : "You find a key. But to what?",
                 "neighbors"    : ["rm_torch", "", "rm_map", ""],
                 "loot"         : ["KEY"]},
                
                {"location"     : "rm_exit",
                 "about"        : "You see an exit!",
                 "neighbors"    : ["", "rm_dark", "", ""],
                 "loot"         : []}
    ]}
    return world

def render(world):

    # Returns (does not print) a string describing the world to the player.

    loc = world["player"]["location"]
    for room in world["world_map"]:
        if room["location"] == loc:
            about = "============================================= \n" + room["about"] + "\n"
            for item in room["loot"]:
                if item not in world["player"]["inventory"]:
                    world["player"]["inventory"].append(item)
            about += "============================================="
            return about

    return "Error rendering world"

def get_options(world):

    # Returns (does not print) a list of valid options available to the player.

    loc = world["player"]["location"]
    options = []
    
    if loc == "rm_dark":
        options = ["TURN BACK", "RISK IT"]
    else:
        for room in world["world_map"]:
            if room["location"] == loc:
                neighbors_pos = room["neighbors"]
        if neighbors_pos[0] != "":
            options.append("NORTH")
        if neighbors_pos[1] != "":
            options.append("SOUTH")
        if neighbors_pos[2] != "":
            options.append("EAST")
        if neighbors_pos[3] != "":
            options.append("WEST")
        if "MAP" in world["player"]["inventory"]:
            options.append("MAP")
    options.append("QUIT")
    return options

def update(world, command):

    # Modifies the game world object and returns it.

    loc = world["player"]["location"]
    if command == "QUIT":
        world["status"] = "quitting"
    elif world["player"]["location"] == "rm_start" and command == "NORTH":
        if "KEY" not in world["player"]["inventory"]:
            print("\nThe door seems to be locked. It won't budge.")
        else:
            print("\nYou try the key. It works!")
            for room in world["world_map"]:
                if room["location"]  == loc:
                    world["player"]["location"] = room["neighbors"][0]
    elif world["player"]["location"] == "rm_start" and command == "EAST":
        if "TORCH" not in world["player"]["inventory"]:
            for room in world["world_map"]:
                if room["location"]  == loc:
                    world["player"]["location"] = "rm_dark"
        else:
            for room in world["world_map"]:
                if room["location"]  == loc:
                    world["player"]["location"] = "rm_lit"
    elif command == "NORTH":
        for room in world["world_map"]:
            if room["location"]  == loc:
                world["player"]["location"] = room["neighbors"][0]
    elif command == "SOUTH":
        for room in world["world_map"]:
            if room["location"]  == loc:
                world["player"]["location"] = room["neighbors"][1]
    elif command == "EAST":
        for room in world["world_map"]:
            if room["location"]  == loc:
                world["player"]["location"] = room["neighbors"][2]
    elif command == "WEST":
        for room in world["world_map"]:
            if room["location"] == loc:
                world["player"]["location"] = room["neighbors"][3]
    elif command == "MAP":
        print(" _______ \n"
              "|       |\n"
              "| x G E |\n"
              "| T S D |\n"
              "| K M x |\n"
              "|_______|")
    elif command == "TURN BACK":
        world["player"]["location"] = "rm_start"
    elif command == "RISK IT":
        fumble = random.randrange(0, 3)
        if fumble == 0:
            for room in world["world_map"]:
                if room["location"]  == loc:
                    world["player"]["location"] = "death2"
                    print("\nWhat could go wrong?")
        elif fumble == 1:
            for room in world["world_map"]:
                if room["location"]  == loc:
                    world["player"]["location"] = "rm_start"
                    print("\nYou blindly fumble around and end up right where you started.")
        elif fumble == 2:
            for room in world["world_map"]:
                if room["location"]  == loc:
                    world["player"]["location"] = "rm_exit"
                    print("\nHere goes nothing!")
    if world["player"]["location"] == "death1":
        print("You are killed by venomous snakes. Bummer!")
        world["status"] = "lose"
    if world["player"]["location"] == "death2":
        print("You fall into a bottomless pit. Whoops.")
        world["status"] = "lose"
    if world["player"]["location"] == "rm_exit":
        world["status"] = "win"
    return ""

def render_ending(world):

    # Returns (does not print) an ending message based on the game's status.

    if world["status"] == "win":
        if ("GOLD") in world["player"]["inventory"]:
            return "You see an exit! \nYou made it out with the gold! You're gonna be rich. \n \nThank you for playing."
        else:
            return "You see an exit! \nYou make it out alive! But without any treasure..."
    elif world["status"] == "quitting":
        return("Sorry to see you go. Play again soon!")
    elif world["status"] == "lose":
        return "Try again!"
    else:
        return "Play again soon."

def choose(options, inventory):

    # Prints valid commands and returns the player's choice.

    print("COMMANDS:")
    for i in range(len(options)):
        print(" - " + options[i])
    if inventory != []:
        print("INVENTORY:")
        for i in range(len(inventory)):
            print(" - " + inventory[i])
    while True:
        print()
        command = input("What do you want to do? ")
        command = command.upper()
        if command == "N":
            command = "NORTH"
        if command == "S":
            command = "SOUTH"
        if command == "E":
            command = "EAST"
        if command == "W":
            command = "WEST"
        if command == "Q":
            command = "QUIT"
        if command == "M":
            command = "MAP"
        if command == "T":
            command = "TURN BACK"
        if command == "R":
            command = "RISK IT"
        if command in options:
            break
        else:
            print()
            print("Invalid command.")
            print()
    return command

def main():

    # Main loop of the game. Utilizes all other functions.

    print(exposition())
    world = create_world()
    while world["status"] == "playing":
        print(render(world))
        options = get_options(world)
        inventory = world["player"]["inventory"]
        command = choose(options, inventory)
        print(update(world, command))
    print(render_ending(world))
    if world["status"] == "quitting":
        return
    input("Press any key to continue.")
    print()
    main()

main()