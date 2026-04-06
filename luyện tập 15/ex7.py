#Bài 7
students = {'Sơn': 10, 'Linh': 9, 'Uyên': 9.5}

def diem_trung_binh(danh_sach_sv):
    if not danh_sach_sv:
        return 0

    tong_diem = sum(danh_sach_sv.values())
    so_luong = len(danh_sach_sv)
    return tong_diem / so_luong

dtb = diem_trung_binh(students)
print(f"Danh sách sinh viên: {students}")
print(f"Điểm trung bình của {len(students)} sinh viên là: {dtb:.2f}")