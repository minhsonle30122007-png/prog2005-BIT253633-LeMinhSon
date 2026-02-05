#BAI 3
n = int(input("Nhập n: "))
a, b = 1,2
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b