from user.UserController import UserController

class QueueController:
    def __init__(self):
        self.ranked_queue = {
            "S": {
                "captain_queue": [],
                "random_queue": []
            },
            "A": {
                "captain_queue": [],
                "random_queue": []
            },
            "B": {
                "captain_queue": [],
                "random_queue": []
            },
            "C": {
                "captain_queue": [],
                "random_queue": []
            },
            "D": {
                "captain_queue": [],
                "random_queue": []
            }
        }
        self.casual_queue = []

    def is_in_queue(self, username):
        if username in self.casual_queue:
            return True
        user = UserController(username)
        if username in self.ranked_queue[user.ranking]["captain_queue"] or \
            username in self.ranked_queue[user.ranking]["random_queue"]:
                return True
        return False

    def add_to_ranked_queue(self, username, queue_type):
        if self.is_in_queue(username):
            return False
        user = UserController(username)
        self.ranked_queue[user.ranking][queue_type].append(username)
        return True

    def add_to_casual_queue(self, username):
        if self.is_in_queue(username):
            return False
        self.casual_queue.append(username)
        return True
    
    def remove_from_ranked_queue(self, username, queue_type):
        user = UserController(username)
        if not username in self.ranked_queue[user.ranking][queue_type]:
            return False
        self.ranked_queue[user.ranking][queue_type].remove(username)
        return True
    
    def remove_from_casual_queue(self, username):
        if not username in self.casual_queue:
            return False
        self.casual_queue.remove(username)
        return True
    
    def get_my_queue(self, username):
        user = UserController(username)
        if username in self.casual_queue:
            return self.casual_queue
        if username in self.ranked_queue[user.ranking]["captain_queue"]:
            return self.ranked_queue[user.ranking]["captain_queue"]
        if username in self.ranked_queue[user.ranking]["random_queue"]:
            return self.ranked_queue[user.ranking]["random_queue"]
        return None
