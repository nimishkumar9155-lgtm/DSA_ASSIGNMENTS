# Directed Weighted Graph using Adjacency List

graph = {
    'A': [('B', 5), ('C', 2)],
    'B': [('D', 4), ('E', 7)],
    'C': [('B', 1), ('E', 3)],
    'D': [('F', 6)],
    'E': [('D', 2), ('F', 1)],
    'F': []
}

# Print Adjacency List
print("Adjacency List Representation:\n")

for node in graph:

    print(f"{node} -> ", end="")

    for neighbor, weight in graph[node]:
        print(f"({neighbor}, weight={weight}) ", end="")

    print()