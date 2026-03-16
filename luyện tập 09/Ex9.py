#Bài 9
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print(f"{self.name} (giống {self.breed}) đang kêu: Gâu Gâu!")


my_dog = Dog("Lu", "Golden Retriever")

my_dog.sound()

print(f"Tên của chú chó là: {my_dog.name}")