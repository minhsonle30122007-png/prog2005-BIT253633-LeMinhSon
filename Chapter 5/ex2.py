#Bài 2
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)

plt.plot(x, x**2, 'b', label='y = x^2')
plt.plot(x, x**3, 'r', label='y = x^3')
plt.legend()
plt.title('So sanh x^2 va x^3')
plt.show()