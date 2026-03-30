#Bài 5
class Flower:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        self._color = new_color

my_flower = Flower("Red")

print(f"Màu hoa ban đầu: {my_flower.get_color()}")

my_flower.set_color("Yellow")
print(f"Màu hoa sau khi đổi: {my_flower.get_color()}")