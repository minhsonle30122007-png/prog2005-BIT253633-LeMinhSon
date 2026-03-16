#Bài 8
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 4)
v2 = Vector(3, 1)

v3 = v1 + v2

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Kết quả v1 + v2 = {v3}")