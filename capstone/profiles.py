class ProfileManager:
    def __init__(self):
        self.users = {}  # hash map

    def add_user(self, user_id, name, interests):
        self.users[user_id] = {
            "name": name,
            "interests": interests
        }

    def get_profile(self, user_id):
        return self.users.get(user_id, "User not found")

    def update_profile(self, user_id, name=None, interests=None):
        if user_id in self.users:
            if name:
                self.users[user_id]["name"] = name
            if interests:
                self.users[user_id]["interests"] = interests