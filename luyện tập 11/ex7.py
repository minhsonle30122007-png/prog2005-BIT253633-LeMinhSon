#Bài 7
name = input("Nhập tên: ")
age = input("Nhập tuổi: ")
staff_id = input("Nhập ID: ")

data = (f"ID: {staff_id}, Tên: {name}, Tuổi: {age}")
with open("nhanvien.txt", "w", encoding="utf-8") as f:
    txt_file.write(data)

    header = ["ID", "Tên", "Tuổi"]
    row = [staff_id, name, age]
    with open("nhanvien.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        writer.writerow(row)

    print("\n--- NỘI DUNG FILE TEXT ---")
    print(data)

    print("\n--- NỘI DUNG FILE CSV ---")
    print(f"{', '.join(header)}\n{', '.join(row)}")

    print("\nĐã lưu file 'nhanvien.txt' và 'nhanvien.csv' thành công!")