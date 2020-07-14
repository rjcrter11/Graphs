"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """

        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # make a queue
        q = Queue()
        # enqueue our starting node
        q.enqueue(starting_vertex)
        # make set to track if we've been here before
        visited = set()
        # while our queue isn't empty
        while q.size() > 0:
            # dequeue w/e at fron of line, this is current_node
            current_node = q.dequeue()
        # if we havent visited this node yet
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
        # print the vertex
                print(current_node)
        # get its neighbors
                neighbors = self.get_neighbors(current_node)
        # for each of the neighbors,
                for neighbor in neighbors:
                    # add to the queue
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # make a stack
        stack = Stack()
        # push on starting node
        stack.push(starting_vertex)
        # make a set to track if weve been here before
        visited = set()
        # while stack not empty
        while stack.size() > 0:
            # pop off w/e on top of the stack, this is our current_node
            current_node = stack.pop()
        # if we haven't visited this vertex before
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
        # print the vertex
                print(current_node)
        # get its neighbors
                neighbors = self.get_neighbors(current_node)
        # for each of neighbors
                for neighbor in neighbors:
                    # add to the top of our stack
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # set a base case: if already visited
        # print vertex
        # add it to the set
        # loop through each vertex getting its neighbors
        # on each of these, call dft_recursive

        # mark this vertex as visited
        # visited.add(starting_vertex)
        # print(starting_vertex)
        # # for each neighbor
        # neighbors = self.get_neighbors(starting_vertex)
        # # if it's not visited
        # for neighbor in neighbors:
        #     # recurse on the neighbor
        #     if neighbor not in visited:
        #         self.dft_recursive(neighbor, visited)

        print(starting_vertex)
        visited.add(starting_vertex)

        for vertex in self.get_neighbors(starting_vertex):
            if vertex not in visited:
                self.dft_recursive(vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO:
        # init a queue
        # enqueue [starting vertex]
        # init visited set()
        # while queue not empty
        # dequeue first in the list -- current_node
        # if it hasn't been visited
        # check if last in list is destination_vertex
        # return if it is
        # else, mark as visited get current's neighbors & enqueue them

        # q = Queue()
        # q.enqueue([starting_vertex])
        # visited = set()

        # while q.size() > 0:
        #     path_list = q.dequeue()
        #     vert = path_list[-1]
        #     if vert not in visited:
        #         if vert == destination_vertex:
        #             return path_list
        #         visited.add(vert)
        #         for next in self.get_neighbors(vert):
        #             path = list(path_list)
        #             path.append(next)
        #             q.enqueue(path)

        # make a queue
        q = Queue()
        # make a set to track nodes
        visited = set()

        path = [starting_vertex]
        q.enqueue(path)

        # while queue isn't empty
        while q.size():
            # dequeue the path at front of line
            current_path = q.dequeue()
            current_node = current_path[-1]
        # if node is target node
            if current_node == destination_vertex:
                # return it
                return current_path
        # if not visited
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
        # get its neighbors
                neighbors = self.get_neighbors(current_node)
        # for each neighbor
                for neighbor in neighbors:
                    # add to our queue
                    # copy list with slice of whole list
                    # so the original path for diff nodes isn't mutated
                    path_copy = current_path[:]
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO:
        # init a stack
        # push [starting vertex]
        # init visited set()
        # while stack not empty
        # pop off top of stack for path list
        # if not visited
        # check if last in list = dest_vert
        # return list if it is
        # else, mark as visited get paths neighbors and push them

        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            path_list = s.pop()
            vert = path_list[-1]
            if vert not in visited:
                if vert == destination_vertex:
                    return path_list
            visited.add(vert)
            for next in self.get_neighbors(vert):
                path = list(path_list)
                path.append(next)
                s.push(path)

    def dfs_recursive(self, vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # TODO:
        # get initial cases of None for visited set and path
        # add starting_vertex to visited
        # add each starting vertex onto path list
        # add base case: if last index of path is dest_vert return it
        # else dfs to get neighbors

        # if visited is None:
        #     visited = set()
        # if path is None:
        #     path = []
        # visited.add(starting_vertex)
        # path = path + [starting_vertex]

        # if starting_vertex == destination_vertex:
        #     return path
        # for next in self.get_neighbors(starting_vertex):
        #     if next not in visited:
        #         new_path = self.dfs_recursive(
        #             next, destination_vertex, visited, path)
        #         if new_path:
        #             return new_path

        # mark our node as visited
        visited.add(vertex)
        # check if its target node
        if vertex == destination_vertex:
            # if so, return
            return path
        if len(path) == 0:
            path.append(vertex)
        # iterate over the neighbors
        neighbors = self.get_neighbors(vertex)
        # check if its visited
        for neighbor in neighbors:
            if neighbor not in visited:
                # if not, recurse with a path
                result = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path + [neighbor])
                if result is not None:
                    # if this recursion returns a path,
                    # return from here
                    return result


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))


'''
Solving Graph problems

1. Describe the problem using graphs terminology
    What are your nodes?
    When are nodes connected?
    What are your connected components
2. Build your graph, or write your getNeighbors()
    Figure out how to get the nodes's edges
3. Choose your algorithm, and apply it
'''
