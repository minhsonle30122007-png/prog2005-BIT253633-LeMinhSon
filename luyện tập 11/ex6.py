#Bài 6
data = {}
for i in range(1):
    ten = input(f"Nhập tên người {i+1}: ")
    tuoi = input(f"Nhập tuổi của {ten}: ")
    data[ten] = int(tuoi)

print("Danh sách:", data)

if data:
    trung_binh = sum(data.values()) / len(data)
    print(f"Tuổi trung bình: {trung_binh: .2f}")
