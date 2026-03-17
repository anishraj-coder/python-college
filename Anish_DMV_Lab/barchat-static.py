import matplotlib.pyplot as plt


X = ['1', '2', '3', '4']
Y = [5, 10, 7, 12]
plt.bar(X, Y,color='orange',edgecolor='black')

plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Static Bar Chart')

plt.show()
