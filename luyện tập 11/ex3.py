#Bài 3
nums = [int(x) for x in input("Nhập các số: ").split()]
chan = [x for x in nums if x % 2 == 0]

print("Các số chẵn:", chan)
print("Tổng các số chẵn:", sum(chan))