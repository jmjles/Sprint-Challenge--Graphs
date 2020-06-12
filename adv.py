from room import Room
from player import Player
from world import World

import random
from util import Queue
from util import Stack
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

#! Usefull Commands
# player.current_room.id
# player.current_room.get_exits()
# player.travel(direction)

traversal_path = []
rooms = {}
reversed = []
opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

#init first room
# While rooms are undescovered
    # if in undescovered room
        # Add room to rooms with it's exits, array
        # get prev move
        # remove prev move (opposite) from current room
    # if all exits are descovered
        # get last move
        # move to last room
        # continue till room with undescovered room
# init room
rooms[player.current_room.id] = player.current_room.get_exits()

while len(rooms)  < len(room_graph) - 1:
    exits = player.current_room.get_exits()
    current = player.current_room.id

    if current not in rooms:

        rooms[player.current_room.id] = exits
        last = reversed[-1]
        rooms[current].remove(last)

    while len(rooms[current]) == 0:
        direction = reversed.pop()
        traversal_path.append(direction)
        player.travel(direction)

        current = player.current_room.id

    direction = rooms[current].pop()
    traversal_path.append(direction)

    reversed.append(opposite[direction])
    player.travel(direction)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
