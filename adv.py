from room import Room
from player import Player
from world import World

import random
from util import Queue
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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
opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# While rooms are undescovered
    # Walk north untill you hit a dead end
    # For prev room
        # set current room to that path
    # If room has unmarked exits
        # Go through it and mark it on the map
        # Come back to original room
        # If there are no more rooms unmarked
            # Set complete to true
while len(rooms)  < len(room_graph):
    exits = player.current_room.get_exits()
    current = player.current_room.id
    for direction in exits:
        rooms[current] = {direction: '?'}
    past = current
    for direction in rooms[current]:
        if rooms[current][direction] == '?':
            while rooms[player.current_room.id]
            player.travel(direction)
            traversal_path.append(direction)
            rooms[past][direction] = current

            player.travel(opposite[direction])
            traversal_path.append(opposite[direction])

    

def bfs(start):
    q = Queue()
    q.enqueue([start])
    visited = set()
    while q.size() > 0:
        v = q.dequeue()
        last = v[-1]
        if last not in visited:
            if last == '?':
                return v
            visited.add(last)
            for neighbor in rooms[current]:
                copy_path = v.copy()
                copy_path.append(neighbor)
                q.enqueue(copy_path)

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
