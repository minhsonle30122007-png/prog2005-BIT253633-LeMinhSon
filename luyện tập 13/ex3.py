#Bài 3
tong = 0
i = 1

print("Các số lẻ từ 1 đến 30:")
while i <= 30:
    if i % 2 != 0:
        print(i, end=" ")
        tong += i
    i += 1

print(f"\nTổng các số lẻ trên là: {tong}")