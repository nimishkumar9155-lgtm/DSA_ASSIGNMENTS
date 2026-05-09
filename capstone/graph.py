class SocialGraph:
    def __init__(self):
        self.graph = {}

    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = []

    def add_connection(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_connection(self, u, v):
        if v in self.graph[u]:
            self.graph[u].remove(v)
        if u in self.graph[v]:
            self.graph[v].remove(u)

    def get_friends(self, user):
        return self.graph.get(user, [])