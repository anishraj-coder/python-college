import matplotlib.pyplot as plt


data = [10, 20, 20, 30, 30, 30, 40, 50]

plt.hist(data, edgecolor='black',bins=5)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Dynamic Histogram")
plt.show()
