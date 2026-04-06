#Bài 8
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = 0
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Lỗi: Giá sản phẩm không thể nhỏ hơn 0!")
        else:
            self.__price = value

p1 = Product("Laptop", 1500)
print(f"Sản phẩm: {p1.name}, Giá: {p1.price}")

p2 = Product("Điện thoại", -500)
print(f"Sản phẩm: {p2.name}, Giá hiện tại: {p2.price}")

p1.price = -100