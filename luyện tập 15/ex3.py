#Bài 3
n = int(input("Nhập vào 1 số nguyên: "))
tong = 1

for i in range(1, n+1):
    tong += i
print(f"Tổng của {n} là: {tong}")