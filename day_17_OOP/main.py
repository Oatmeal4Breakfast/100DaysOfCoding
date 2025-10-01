class User:
    def __init__(self, id: int, username: str) -> None:
        """initialize the attributes"""
        self.id: int = id
        self.username: str = username
        self.followers: int = 0
        self.following: int = 0

    def follow(self, user) -> None:
        user.followers += 1
        self.following += 1


user_1 = User(id=1, username="thoughts")
user_2 = User(id=2, username="ideas")

user_1.follow(user_2)

print(
    f" user_1 has the following properties id: {user_1.id} and username: {user_1.username}"
)

print(f"user_1 has {user_1.followers} followers")
print(f"user_1 is following {user_1.following} people")
print(f"user_2 has {user_2.followers} followers")
print(f"user_2 is following {user_2.following} people")

