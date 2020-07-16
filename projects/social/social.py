import random
from collections import deque
import time


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fishere_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_indx = random.randint(i, len(l) - 1)
            l[random_indx], l[i] = l[i], l[random_indx]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # use num_users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        # make a list w/ all POSSIBLE friendships
        # 5 users
        # [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5)]
        friendships = []
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, num_users + 1):
                friendship = (user, friend)
                friendships.append(friendship)

        # Shuffle the list
        self.fishere_yates_shuffle(friendships)
        # Take as many as we need
        total_friendships = num_users * avg_friendships

        random_friendships = friendships[:total_friendships//2]

        # add to self.friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def linear_populate_graph(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # use num_users
        for user in range(num_users):
            self.add_user(user)

        # linear way to add number of friendships we need
        # as long as we haven't made al lthe friendships we need
        target_number_friendships = num_users * avg_friendships
        friendships_created = 0
        while friendships_created < target_number_friendships:
            # pick 2 random numbers btw 1 and last_id
            friend_one = random.randint(1, self.last_id)
            friend_two = random.randint(1, self.last_id)
        # try to create that friendship
            friendship_was_made = self.add_friendship(friend_one, friend_two)
        # if we can, increment friendship counter by 2
            if friendship_was_made:
                friendships_created += 2

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        Plan: BFT, use dict as visited
        """
        # visited is graph
        # Node: users and users friends
        # Edges: friendship connects
        # BFT for fastest path between

        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # q = deque()
        # path = [user_id]
        # q.append(path)

        # while len(q) > 0:
        #     path = q.popleft()
        #     user = path[-1]

        #     if user not in visited:
        #         visited[user] = path

        #         for friend in self.friendships[user]:
        #             new_path = list(path)
        #             new_path.append(friend)
        #             q.append(new_path)

        q = deque()
        q.append([user_id])

        # While q not empty
        while len(q):
            # dequeue current path
            current_path = q.popleft()

            # grab last vertex from path
            current_user = current_path[-1]
            # if not been visited
            if current_user not in visited:
                # add to dictionary
                visited[current_user] = current_path
            # { friend_id: path }
                friends = self.friendships[current_user]
            # then enqueue path to each of our neighbors
                for friend in friends:
                    path_to_friend = current_path + [friend]

                    q.append(path_to_friend)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()

    num_users = 10000
    avg_friendships = 5

    # start_time = time.time()
    # sg.populate_graph(num_users, avg_friendships)
    # end_time = time.time()
    # print(f"Pop graphO(n^2): {end_time - start_time}")
    start_time = time.time()
    sg.linear_populate_graph(num_users, avg_friendships)
    end_time = time.time()
    print(f"Pop graph O(n): {end_time - start_time}")

    # print("Friendships: ", sg.friendships)
    #connections = sg.get_all_social_paths(1)
    # print("Connections: ", connections)

    # what percentage of total users are in our extended social network?

    # how many people we know, divided by how many people there are

    #print(f'{(len(connections) - 1) / 10000 * 100}%')

    # Whats the avg degree of separation btw a user and those in his/her extended network?
    # Avg length of each path in connections/ avg length of a path to each user
    # traverse a user's extended connections, gather lengths, sum,
    total_lengths = 0
    # for friend in connections:
    # n = [len(v) for k, v in connections.items() if k != 1]
    # print(sum(n) / len(n))
    # sum([len(connection) for connection in connections])/len(connections)
    #total_lengths += len(connections[friend])
    # divide by number of friends in connected component aka extended social network

    # print(
    # f'Average degree of separation: {total_lengths / len(connections)}')
