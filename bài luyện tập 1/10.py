#Bài 10
import os

def save_product():
    data = input("Nhập Code;Name;Price: ")
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(data + "n")

def show_sorted():
    if not os.path.exists("data.txt"): return

    with open("data.txt", "r", encoding="utf-8") as f:
        lines = [line.strip().split(";") for line in f if line.strip()]

    lines.sort(key=lambda x: float(x[2]), reverse=True)

    print("Danh sách sản phẩm (Giá giảm dần):")
    for p in lines:
        print("{p[0]} - {p[1]} - {p[2]}")

save_product()
show_sorted()