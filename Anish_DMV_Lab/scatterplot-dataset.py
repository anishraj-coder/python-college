import numpy as np
import matplotlib.pyplot as plt

# 1. Create a cluster with a Negative Correlation
# Generate 50 random x values
x1 = np.random.rand(50) 
# Create y values with a negative trend (y = -x) plus some noise
y1 = -x1 + np.random.normal(0, 0.1, 50)

# 2. Create a second cluster to satisfy the "clusters" requirement
x2 = np.random.uniform(0.1, 0.3, 10)
y2 = np.random.uniform(0.5, 0.7, 10)

# 3. Add an Outlier
# This point will be far away from the clusters and the trendline
x_outlier = np.array([0.9])
y_outlier = np.array([1.5])

# Combine all data points
x = np.concatenate([x1, x2, x_outlier])
y = np.concatenate([y1, y2, y_outlier])

# Create the plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', alpha=0.7, label='Data Points')

# Labels and Title
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter Plot: Negative Correlation, Clusters, and Outliers')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Show the plot
plt.show()
