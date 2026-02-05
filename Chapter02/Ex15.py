#BAI 15
n = int(input("Nhập một số nguyên dương: "))
tong = 0
while n > 0:
    tong += n % 10
    n //= 10
print(f"Tổng các chữ số là: {tong}")