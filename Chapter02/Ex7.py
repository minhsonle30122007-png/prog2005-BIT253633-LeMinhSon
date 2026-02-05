#Bai 7
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
while b:
    a, b = b, a % b
print(f"Ước số chung lớn nhất là: {a}")