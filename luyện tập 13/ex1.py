#Bài 1
n = int(input("Nhập một số: "))

if n < 0:
    print("Lỗi: Số nhập vào không được là số âm!")
else:
    du = n % 2
    print(f"Phần dư của khi chia cho 2 là: ")