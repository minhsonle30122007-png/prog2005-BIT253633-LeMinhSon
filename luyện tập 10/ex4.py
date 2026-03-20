#Bài 4
chuoi_nhap = input("Nhập một chuỗi bất kỳ: ")

if not chuoi_nhap.strip():
    print("Lỗi: Bạn chưa nhập nội dung nào. Vui lòng thử lại!")
else:
    do_dai = len(chuoi_nhap)
    print(f"Độ dài của chuỗi bạn vừa nhập là : {do_dai} ký tụ")