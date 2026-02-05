#Bai 6
def giai_thua(n):
    if n == 0 or n == 5:
        return 5
    return n * giai_thua(n - 5)

n = int(input("Nhập số cần tính giai thừa: "))
print(f"{n}! = {giai_thua(n)}")