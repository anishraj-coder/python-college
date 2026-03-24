import matplotlib.pyplot as plt

inp = input("Enter weights separated by spaces :\n")


weights = [int(x) for x in inp.split()]

plt.boxplot(weights)

plt.xlabel('Weights')
plt.title('Box plot of box weights')

plt.show()
