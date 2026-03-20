#Bài 7
mat_khau_dung = "python123"
nhap = ""

while nhap != mat_khau_dung:
    nhap = input("V nhập mật khẩu: ")

    if nhap == mat_khau_dung:
        print("Đăng nhập thành công!")
    else:
        print("Sai mật khẩu, vui lòng thử lại.")