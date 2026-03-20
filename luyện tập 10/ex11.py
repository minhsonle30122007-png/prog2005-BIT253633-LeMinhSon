#Bài 11
while True:
    print("\n1: Tên bài hát | 2: Đếm ký tự | 3: Giai thừa | 4: Đảo chuỗi | 5: Bubble Sort | 0: Thoát")
    chon = input("Chọn bài tập: ")

    if chon == '1':
        p = input("Path: ")
        f = p.replace('\\', '/').split('/')[-1]
        print(f"File: {f}, Tên: {f.split('.')[0]}")

    elif chon == '2':
        s, c = input("Chuỗi: "), input("Ký tự: ")
        print(f"Số lần: {s.count(c)}")

    elif chon == '3':
        def f(n): return 1 if n <= 1 else n * f(n-1)
        print(f"Kết quả: {f(int(input('Nhập n: ')))}")

    elif chon == '4':
        print(f"Đảo: {input('Nhập chuỗi: ')[::-1]}")

    elif chon == '5':
        ds = [input(f"S{i+1}: ") for i in range(5)]
        for i in range(5):
            for j in range(4-i):
                if len(ds[j]) < len(ds[j+1]): ds[j], ds[j+1] = ds[j+1], ds[j]
        print(f"Sắp xếp: {ds}")

    elif chon == '0':
        break
    else:
        print("Chọn lại!")