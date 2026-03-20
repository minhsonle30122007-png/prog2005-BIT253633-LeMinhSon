#Bài 10
n = len(ds)

print("\n--- Quá trình sắp xếp ---")
for i in range(n):
    for j in range(0, n - i - 1):
        if len(ds[j]) < len(ds[j + 1]):
            ds[j], ds[j + 1] = ds[j + 1], ds[j]
            print(f"Bước {i+1}.{j+1}: {ds}")

print("\nKết quả cuối cùng:", ds)