import random
from collections import deque


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
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

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

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # visited is graph
        # Node: users and users friends
        # Edges: friendship connects
        # BFT for fastest path between

        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = deque()
        path = [user_id]
        q.append(path)

        while len(q) > 0:
            path = q.popleft()
            user = path[-1]

            if user not in visited:
                visited[user] = path

                for friend in self.friendships[user]:
                    new_path = list(path)
                    new_path.append(friend)
                    q.append(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("Friendships: ", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("Connections: ", connections)
