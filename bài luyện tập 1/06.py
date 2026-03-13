#Bài 6
import math
s = "5; 7; 8; -2; 8; 11; 13; 9; 10"
nums = [int(x) for x in s.split("; ")]

is_prime = lambda n: n > 1 and all(n % i for i in range(2, int(math.sqrt(n)) + 1))

print("Các số trong chuỗi:")
print(*nums, sep="\n")

chan = [x for x in nums if x % 2 == 0]
am = [x for x in nums if x < 0]
nt = [x for x in nums if is_prime(x)]
trung_binh = sum(nums) / len(nums)

print(f"\nSố lượng số chẵn: {len(chan)}")
print(f"Số lượng số âm: {len(am)}")
print(f"Số lượng số nguyên tố: {len(nt)}")
print(f"Giá trị trung bình: {trung_binh:.2f}")