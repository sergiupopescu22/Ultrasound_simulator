import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Example data for the 3D graph
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Function to define the first level (surface 1)
Z1 = np.sin(np.sqrt(X**2 + Y**2))

# Function to define the second level (surface 2)
Z2 = Z1 - 5

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the first level (surface 1)
ax.plot_surface(X, Y, Z1, cmap='viridis', label='Surface 1')

# Plot the second level (surface 2)
ax.plot_surface(X, Y, Z2, cmap='plasma', label='Surface 2')

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Graph with Multiple Levels')

# Add a legend


# Show the plot
plt.show()

