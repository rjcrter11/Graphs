from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []
reverse_traversal = []
visited = {}
go_back = {"n": "s", "s": "n", "e": "w", "w": "e"}

current_room = player.current_room


def create_visited_dictionary(room, exits):
    if room.id not in visited:
        for ext in room.get_exits():
            exits[ext] = "?"
            visited[room.id] = exits


def get_next_move(room):
    exit_room = visited[room.id]

    for move in exit_room:
        if exit_room[move] == '?' and room.get_room_in_direction(move).id not in visited:
            return move

    return None


def travel_maze(direction):
    player.travel(direction)
    traversal_path.append(direction)
    reverse_traversal.append(go_back[direction])


def find_new_exits(direction):
    while direction is None:
        back = reverse_traversal.pop()
        traversal_path.append(back)
        player.travel(back)
        next_room = player.current_room

        if '?' in visited[next_room.id].values():
            return next_room


while len(visited) < len(room_graph):
    exits = {}
    create_visited_dictionary(current_room, exits)

    next_move = get_next_move(current_room)

    if next_move is not None:
        travel_maze(next_move)
        previous_room = current_room
        current_room = player.current_room

        new_exits = {}
        create_visited_dictionary(current_room, new_exits)

        visited[previous_room.id][next_move] = current_room.id
        visited[current_room.id][go_back[next_move]] = previous_room.id

    else:
        current_room = find_new_exits(next_move)


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
