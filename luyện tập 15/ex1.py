#Bài 1
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai:  "))

tong = a + b
hieu = a - b
tich = a * b
if b == 0:
    thuong = a / b
else:
    thuong = "Không thể chia cho 0"

print(f"tổng: {a+b} = {tong}")
print(f"hiệu: {a+b} = {hieu}")
print(f"tích: {a+b} = {tich}")
print(f"thương: {a+b} = {thuong}")
