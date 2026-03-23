#Bài 2
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [23,12,10,9,4,3,2]
target = input("Nhập chuỗi cần tìm: ")
pos = binary_search(arr, target)

if pos != -1:
    print(f"Tìm thấy '{target}' tại vị trí index: {pos}")
else:
    print("Không tìm thấy chuỗi trong danh sách.")