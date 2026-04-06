#Bài 4
diem_1 = float(input("Nhập điểm môn 1: "))
diem_2 = float(input("Nhập điểm môn 2: "))
diem_3 = float(input("Nhập điểm môn 3: "))

diem_tb = (diem_1 + diem_2 + diem_3)/3
print(f"Điểm trung bình là : {diem_tb}")

if diem_tb >= 8.0:
    print("Xếp loại : giỏi ")
elif 6.5 <= diem_tb <= 7.9:
    print("Xếp loại: khá")
elif 5.0 <= diem_tb <= 6.4:
    print("Xếp loại: trung bình")
else:
    print("Xếp loại: yếu")
