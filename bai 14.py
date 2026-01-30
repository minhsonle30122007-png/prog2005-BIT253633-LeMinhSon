#Bai 14
import math

try:
    num = float(input("Nhập một số: "))
    if num < 0:
        print("Lỗi: Không thể tính căn bậc hai của số âm")
    else:
        print(math.sqrt(num))
except ValueError:
    print("Lôi: Dữ liệu nhập vào không phải là số")