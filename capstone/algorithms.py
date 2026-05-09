from collections import deque

def bfs_shortest_path(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))

    return None

def dfs_limited(graph, start, depth, visited=None):
    if visited is None:
        visited = set()

    if depth < 0:
        return []

    visited.add(start)
    result = [start]

    if depth == 0:
        return result

    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_limited(graph, neighbor, depth - 1, visited))

    return result