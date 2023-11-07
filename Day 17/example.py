class User:
    def __init__(self, user_id, user_name):
        print("New User!")
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Roberto")
user_2 = User("002", "Maria")

user_1.follow(user_2)
print(user_1)
