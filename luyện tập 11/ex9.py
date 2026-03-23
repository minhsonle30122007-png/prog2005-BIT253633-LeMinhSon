#Bài 9
def nhap_ma_tran(ten, hang, cot):
    mt = []
    for i in range(hang):
        hang_moi = []
        for j in range(cot):
            val = input(f"Nhập {ten}[{i}][{j}]: ").strip()
            if not val: raise ValueError("Lỗi: Giá trị không được để trống!")
            hang_moi.append(int(val))
        mt.append(hang_moi)
    return mt


try:
    r, c = int(input("Số hàng: ")), int(input("Số cột: "))

    print("--- Ma trận A ---")
    A = nhap_ma_tran("A", r, c)
    print("--- Ma trận B ---")
    B = nhap_ma_tran("B", r, c)

    print("\nKết quả A + B:")
    for i in range(r):
        tong_hang = [A[i][j] + B[i][j] for j in range(c)]
        print(tong_hang)

except ValueError as e:
    print(e)