def recommend_users(profiles, graph, user):
    user_interests = set(profiles[user]["interests"])
    suggestions = []

    for other in profiles:
        if other != user and other not in graph[user]:
            common = user_interests.intersection(profiles[other]["interests"])
            suggestions.append((other, len(common)))

    # sort by common interests
    suggestions.sort(key=lambda x: x[1], reverse=True)

    return suggestions