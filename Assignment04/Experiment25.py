# Graph using Adjacency List

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Visited Set
visited = set()

# DFS Function
def dfs(node):

    if node not in visited:

        print(node, end=" ")

        visited.add(node)

        for neighbor in graph[node]:

            dfs(neighbor)


# Main
start_node = 'A'

print("DFS Traversal:", end=" ")

dfs(start_node)