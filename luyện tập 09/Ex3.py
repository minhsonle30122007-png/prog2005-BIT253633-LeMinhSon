#Bài 3
name= input('Nhập họ tên cần chuẩn hóa:')
name= name.strip()
name= ' '.join(name.split())
name= name.title()
print(f"Tên người dùng sau khi chuẩn hóa:'{name}'")