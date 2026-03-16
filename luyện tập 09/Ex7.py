#Bài 7
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, person_str):
        name, age = person_str.split("-")

        return cls(name, int(age))

    def __str__(self):
        return f"Tên: {self.name}, Tuổi: {self.age}"



p1 = Person("Lan", 25)
print(f"Cách 1: {p1}")

input_str = "Nam-20"
p2 = Person.from_string(input_str)
print(f"Cách 2: {p2}")