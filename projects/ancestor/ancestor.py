from collections import deque


def earliest_ancestor(ancestors, starting_node):
    # TODO:
    # Init a graph
    # populate it with the given values
    # loop so that children have lists of parents
    # Init a stack
    # Append starting node to stack
    # Init a visited set
    # while stack isn't empty
    # pop node off the stack
    # Check if its in visited set -- if not, add it
    # append the key's smallest value to the stack
    # Check if its not in the graph --
    # Numbers that aren't keys will be oldest ancestors
    # if visited set > 1 (more than what just got popped off and put in the set)
    # return the node
    # That's the oldest ancestor
    # else return -1 (it's a number with no ancestors)

    graph = {}

    for parent, child in ancestors:
        if child not in graph:
            graph[child] = []
        graph[child].append(parent)

    s = deque()
    s.append(starting_node)

    visited = set()

    while len(s):
        node = s.pop()

        if node not in visited:
            visited.add(node)

            if node not in graph.keys():
                if len(visited) == 1:
                    return -1

                else:
                    return node
            s.append(graph[node][0])
