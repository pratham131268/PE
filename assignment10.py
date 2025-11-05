import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 35]
y2 = [15, 18, 22, 27, 33]
sizes = [30, 25, 20, 15, 10]
labels = ['A', 'B', 'C', 'D', 'E']

plt.figure(figsize=(10,6))

plt.subplot(2,2,1)
plt.plot(x, y1, color='green')
plt.title("Line Chart")

plt.subplot(2,2,2)
plt.bar(x, y2, color='orange')
plt.title("Bar Chart")

plt.subplot(2,2,3)
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")

plt.tight_layout()
plt.show()
