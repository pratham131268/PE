import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [20000, 25000, 22000, 27000, 30000]
profit = [4000, 5000, 3500, 6000, 7000]

plt.bar(months, sales, color='lightblue', label='Sales')
plt.plot(months, profit, color='red', marker='o', label='Profit')
plt.title("Sales and Profit Comparison")
plt.xlabel("Months")
plt.ylabel("Amount (₹)")
plt.legend()
plt.show()
