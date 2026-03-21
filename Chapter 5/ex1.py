#Bài 1
import matplotlib.pyplot as plt

loai = ['X.Sắc', 'Giỏi', 'T.Bình', 'Yếu', 'Kém']
so_luong = [6, 10, 12, 4, 1]

plt.bar(loai, so_luong)
plt.title('KET QUA HOC TAP')
plt.xlabel('Xep loai')
plt.ylabel('So luong')
plt.show()