#Bài 5
my_dict = {"name": "lê minh sơn", "age": 18}
key_to_check = input("Nhập key cần tìm: ")

if key_to_check in my_dict:
    print(f"Key '{key_to_check}' có tồn tại.Gía trị: {my_dict[key_to_check]}")
else:
    print(f"Key '{key_to_check}' không tồn tại.")