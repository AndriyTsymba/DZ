
class UserNotFoundError(Exception):
    pass
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserDatabase:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            raise UserNotFoundError(f"User '{username}' wasn't found ((")
database = UserDatabase()
user1 = User("Igor", "adjgefwtfd@gmail.com")
user2 = User("Kostiy", "just@gmail.com")
database.add_user(user1)
database.add_user(user2)
try:
    user = database.get_user("dimon")
    print(f"Username: {user.username}, Email: {user.email}")
except UserNotFoundError as e:
    print(e)