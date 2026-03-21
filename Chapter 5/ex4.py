#Bài 4
import matplotlib.pyplot as plt
import pandas as pd

top10 = df.sort_values('area_total_km2', ascending=False).head(10)

plt.barh(top10['city'][::-1], top10['area_total_km2'][::-1], color='skyblue')
plt.title('Top 10 Thanh pho lon nhat California')
plt.xlabel('Dien tich (km2)')
plt.ylabel('Thanh pho')
plt.show()