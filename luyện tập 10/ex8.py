#Bài 8
danh_sach = input("Chuỗi {i+1}: ")
n = len(danh_sach)

for i in range(n):
    for j in range(0, n-i-1):
        if len(danh_sach[j]) < len(danh_sach[j+1]):
            danh_sach[j], danh_sach[j+1] = danh_sach[j+1], danh_sach[j]
            print(f"Bước {i+1}.{j+1}: {danh_sach}")

print("\nKết quả cuối cùng:", danh_sach)