class User:
    def __init__(self):
        self.users = {}

    def register_user(self, user_id):
        self.users[user_id] = {"borrowed_books": []}

    def borrow_book(self, user_id, title):
        if user_id in self.users:
            self.users[user_id]["borrowed_books"].append(title)

    def return_book(self, user_id, title):
        if user_id in self.users and title in self.users[user_id]["borrowed_books"]:
            self.users[user_id]["borrowed_books"].remove(title)
