from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from collections import deque

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
start = player.current_room

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []

reverse_traversal = []

visited = {}

go_back = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}
current_room = start


if current_room.id not in visited:

    room_exits = current_room.get_exits()
    print("Exits: ", room_exits)
    exits = {}
    for ext in room_exits:
        exits[ext] = "?"
        visited[current_room.id] = exits
    print("Visited: ", visited)

while len(visited) < len(room_graph) - 1:
    current = current_room.id
    exit_room = visited[current]
    print("Exits in while loop", exit_room)

    for move in exit_room:
        if exit_room[move] == '?' and current_room.get_room_in_direction(move) not in visited:
            next_room = move
        else:
            next_room = None
    if next_room is None:
        break  # go backwards to look for an exit
    else:
        player.travel(next_room)
        traversal_path.append(next_room)

        reverse_traversal.append(go_back[next_room])
        prev_room = current_room
        current_room = player.current_room
        print("Previous room: ", prev_room.id)

        next_exits = {}
        for ext in current_room.get_exits():
            next_exits[ext] = '?'
            visited[current_room.id] = next_exits


print("Traversal_path", traversal_path)
print("Visited: ", visited)
# TRAVERSAL TEST
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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
