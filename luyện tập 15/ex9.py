#Bài 9
content = input("Nhập chuỗi ký tự: ")

with open("data.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("Đã lưu vào file data.txt thành công!")