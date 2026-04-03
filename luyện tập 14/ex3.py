#Bài 3
def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

nums = list(map(int, input("Nhập mảng các số tự nhiên (cách nhau bởi dấu cách): ").split()))

so_le = [x for x in nums if x % 2 != 0]
print(f"Các số lẻ: {so_le} - Tổng số lượng: {len(so_le)}")

so_nt = [x for x in nums if la_so_nguyen_to(x)]
print(f"Các số nguyên tố: {so_nt}")