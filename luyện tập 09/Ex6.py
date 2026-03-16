#Bài 6
class Product:
    def __init__(self, prince):
        self.prince = prince
@property
def prince(self):
    return self.__prince
@prince.setter
def prince(self, value):
    if value > 0:
        self.__prince = value
def __str__(self):
    return f"Prince({self.prince})"
sp1 = Product(20)
print(sp1)