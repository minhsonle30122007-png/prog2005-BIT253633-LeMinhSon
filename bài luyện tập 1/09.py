#Bài 9
class Students:
    def __init__(self, student, price):
        self.student = student
        self.price = price

    def display(self):
        print("Sinh vien {self.student} co diem la  {self.price}")
h = Students("Minh Sơn", 10)
h.display()