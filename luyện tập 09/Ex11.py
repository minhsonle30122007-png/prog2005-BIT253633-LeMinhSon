#Bài 11
class SinhVien:
    so_luong = 0

    def __init__(self, ten):
        self.ten = ten
        SinhVien.so_luong += 1

    @classmethod
    def hien_thi_tong_so_sv(cls):
        print(f"Tổng số sinh viên hiện có: {cls.so_luong}")


SinhVien.hien_thi_tong_so_sv()

sv1 = SinhVien("Sơn")
sv2 = SinhVien("Uyên")
sv3 = SinhVien("Thỏ")

SinhVien.hien_thi_tong_so_sv()