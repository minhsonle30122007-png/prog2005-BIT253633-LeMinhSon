#Bài 1
arr = [input(f"Chuỗi {i+1}: ") for i in range(5)]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and len(arr[j]) < len(key):
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
    print(f"Bước {i}: {arr}")

print("Kết quả:", arr)