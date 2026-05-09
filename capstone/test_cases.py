
from profiles import ProfileManager
from graph import SocialGraph
from algorithms import bfs_shortest_path, dfs_limited
from recommendations import recommend_users

# Initialize
pm = ProfileManager()
sg = SocialGraph()

# ---------------- ADD USERS ----------------
print("\n--- Adding Users ---")

pm.add_user(1, "A", ["music", "sports"])
pm.add_user(2, "B", ["music", "movies"])
pm.add_user(3, "C", ["sports", "travel"])
pm.add_user(4, "D", ["travel", "food"])
pm.add_user(5, "E", ["music", "food"])
pm.add_user(6, "F", ["sports", "movies"])

for i in pm.users:
    print(f"User {i} added: {pm.users[i]['name']}")

# Add graph nodes
for i in range(1, 7):
    sg.add_user(i)

# ---------------- UPDATE PROFILE ----------------
print("\n--- Updating Profile ---")
pm.update_profile(1, interests=["music", "gaming"])
print("User 1 interests updated to:", pm.users[1]["interests"])

# ---------------- ADD CONNECTIONS ----------------
print("\n--- Creating Connections ---")

sg.add_connection(1, 2)
print("1 ↔ 2")

sg.add_connection(1, 3)
print("1 ↔ 3")

sg.add_connection(2, 4)
print("2 ↔ 4")

sg.add_connection(3, 5)
print("3 ↔ 5")

sg.add_connection(4, 6)
print("4 ↔ 6")

# ---------------- REMOVE CONNECTION ----------------
print("\n--- Removing Connection ---")
sg.remove_connection(2, 4)
print("Connection removed: 2 ↔ 4")

# ---------------- SHOW PROFILES ----------------
print("\n--- Showing Profiles ---")
for i in [1, 3, 5]:
    print(f"User {i}:", pm.get_profile(i))

# ---------------- BFS ----------------
print("\n--- BFS Shortest Path ---")
path1 = bfs_shortest_path(sg.graph, 1, 5)
path2 = bfs_shortest_path(sg.graph, 1, 6)

if path1:
    print("From 1 to 5:", " → ".join(map(str, path1)))
    print("Degrees of separation:", len(path1) - 1)

if path2:
    print("From 1 to 6:", " → ".join(map(str, path2)))
    print("Degrees of separation:", len(path2) - 1)

# ---------------- DFS ----------------
print("\n--- DFS Exploration ---")

dfs2 = dfs_limited(sg.graph, 1, 2)
print("Depth 2:", dfs2)

dfs3 = dfs_limited(sg.graph, 1, 3)
print("Depth 3:", dfs3)

# ---------------- RECOMMENDATIONS ----------------
print("\n--- Friend Recommendations for User 1 ---")

recs = recommend_users(pm.users, sg.graph, 1)

for user, score in recs:
    if score > 0:
        print(f"User {user} (Common interests: {score})")
