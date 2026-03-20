#Bài 3
def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*tinh_giai_thua(n-1)

try:
    so_nhap = int(input("Nhập một số nguyên dương: "))

    if so_nhap < 0:
        print("Nhập số hơn hoặc bằng 0.")
    else:
        ket_qua = tinh_giai_thua(so_nhap)
        print(f"Giai thừa của {so_nhap} là: {ket_qua}")
except ValueError:
    print("Lỗi: Vui lòng chỉ nhập số nguyên.")