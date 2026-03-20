#Bài 9
class Vehicle:
    _count = 0

    def __init__(self, brand, speed):
        self.brand = brand
        if speed < 0: raise ValueError("Tốc độ không thể âm!")
        self._speed = speed
        Vehicle._count += 1

    @property  # Getter
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, v):
        if v > 300: raise ValueError("Quá tốc độ cho phép!")
        self._speed = v

    def move(self):
        return f"{self.brand} đang chạy."

    @classmethod
    def total(cls):
        return f"Tổng xe: {cls._count}"

    @staticmethod
    def check_safety(s):
        return s <= 120

    def __str__(self):
        return f"{self.brand} - {self._speed}km/h"

    def __eq__(self, other):
        return self._speed == other._speed


class Car(Vehicle):
    def __init__(self, brand, speed, fuel):
        super().__init__(brand, speed)
        self.fuel = fuel

    def __str__(self): return super().__str__() + f" ({self.fuel})"

try:
    c1 = Car("Toyota", 80, "Xăng")
    c2 = Car("Tesla", 80, "Điện")

    print(f"Đối tượng: {c1}")
    c1.speed = 100
    print(f"So sánh ==: {c1 == c2}")
    print(c1.move())
    print(Vehicle.total())
    print(f"An toàn? {Vehicle.check_safety(150)}")

    c1.speed = -10
except ValueError as e:
    print(f"Lỗi: {e}")