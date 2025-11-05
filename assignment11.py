import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = np.sin(x)
data = np.random.randn(1000)

plt.figure(figsize=(10,6))

plt.subplot(3,1,1)
plt.scatter(x, y, color='purple')
plt.title("Scatter Plot")

plt.subplot(3,1,2)
plt.plot(x, y, color='blue')
plt.title("Line Graph")

plt.subplot(3,1,3)
plt.hist(data, bins=20, color='green')
plt.title("Histogram")

plt.tight_layout()
plt.show()
