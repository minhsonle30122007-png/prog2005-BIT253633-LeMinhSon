#Bai 13
try:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    print(a/b)
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0")
except ValueError:
    print("Lỗi: Dữ Liệu nhập vào không hợp lệ")