#Bài 3
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E']
sizes  = [30, 25, 15, 20, 10]
colors = ['gold', 'lightskyblue', 'lightcoral', 'lightgreen', 'orange']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('DOANH SO THEO SAN PHAM')
plt.show()