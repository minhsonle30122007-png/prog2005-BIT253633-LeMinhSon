 #Bài 4
import math

nums = [int(x) for x in input("Nhập danh sách số: ").split()]

k = int(input("Nhập k: "))
print(f"Số lần {k} xuất hiện: {nums.count(k)}")

def check_nt(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

print(f"Tổng số nguyên tố: {sum(x for x in nums if check_nt(x))}")

nums.sort()
print(f"Danh sách đã sắp xếp: {nums}")
nums.clear()
print("Danh sách sau khi xóa:", nums)