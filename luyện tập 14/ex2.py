#Bài 2
danh_sach_ten = []
for i in range(5):
    ten = input(f"Nhập tên người thứ {i+1}: ")
    danh_sach_ten.append(ten)

print("Danh sách ban đầu:", danh_sach_ten)

if len(danh_sach_ten) >= 2:
    ten_bi_xoa = danh_sach_ten.pop(1)
    print(f"Đã xóa: {ten_bi_xoa}")

print("Danh sách sau khi xóa người thứ hai:", danh_sach_ten)