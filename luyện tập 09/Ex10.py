class SinhVien:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem

    def __eq__(self, other):
        if isinstance(other, SinhVien):
            return self.diem == other.diem
        return False

    def __str__(self):
        return f"{self.ten} ({self.diem} điểm)"


sv1 = SinhVien("An", 8.5)
sv2 = SinhVien("Bình", 8.5)
sv3 = SinhVien("Chi", 9.0)

print(f"Sinh viên 1: {sv1}")
print(f"Sinh viên 2: {sv2}")
print(f"Sinh viên 3: {sv3}")
print("-" * 20)

if sv1 == sv2:
    print("Kết quả: sv1 và sv2 có điểm bằng nhau.")
else:
    print("Kết quả: sv1 và sv2 có điểm khác nhau.")

if sv1 == sv3:
    print("Kết quả: sv1 và sv3 có điểm bằng nhau.")
else:
    print("Kết quả: sv1 và sv3 có điểm khác nhau.")