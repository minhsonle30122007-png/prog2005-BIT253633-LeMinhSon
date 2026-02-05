#BAI 11
dtb = float(input("Nhập điểm trung bình: "))
if dtb >= 9:
    print("Xếp loại: Giỏi")
elif 6.5 <= dtb <= 8.9:
    print("Xếp loại: Khá")
elif 5.0 <= dtb <= 6.4:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")