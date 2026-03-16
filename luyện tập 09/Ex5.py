#Bài 5
class User:
    def __init__(self, user_id):
        self.id = user_id

@property
def id(self):
    return self._id
u = User(10)
print(f"ID của người dùng là: {u.id}")