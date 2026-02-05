#BAI 12
n = int(input("Nhập n: "))
tong = 0
for i in range(1, n + 1, 2):
    if i % 2 != 0:
        tong += i
print(tong)