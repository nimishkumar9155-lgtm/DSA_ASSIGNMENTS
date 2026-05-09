from collections import deque

# Graph using Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS Function
def bfs(start):

    visited = set()

    queue = deque([start])

    visited.add(start)

    print("BFS Traversal:", end=" ")

    while queue:

        node = queue.popleft()

        print(node, end=" ")

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)


# Main
start_node = 'A'

bfs(start_node)