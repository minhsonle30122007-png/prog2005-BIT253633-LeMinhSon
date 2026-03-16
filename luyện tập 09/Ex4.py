#Bai 4
string = input('Nhập một chuỗi bất kỳ:')
count_upper = 0
count_lower = 0
count_so = 0
count_KTDB = 0
count_KTKC = 0
count_nguyenam = 0
count_phuam = 0

for i in string:
    if i.isupper():
        count_upper = count_upper + 1
    elif i.islower():
        count_lower = count_lower + 1
    elif i.isdigit():
        count_so = count_so + 1
    elif i.isdigit():
        count_KTDB = count_KTDB + 1
    elif i.isalpha():
        count_KTKC = count_KTKC + 1
    elif i.isnumeric():
        count_nguyenam = count_nguyenam + 1
    elif i.isspace():
        count_phuam = count_phuam + 1

print("-" * 30)
print(f"1. Số lượng chữ in hoa:{count_upper}")
print(f"2. Số lượng chữ in thường:{count_lower}")
print(f"3. Số lượng chữ số:{count_so}")
print(f"4. Số lượng ký tự đặc biệt:{count_KTDB}")
print(f"5. Số lượng ký tự khoảng cách:{count_KTKC}")
print(f"6. Số lượng nguyên âm:{count_nguyenam}")
print(f"7. Số lượng phụ âm:{count_phuam}")