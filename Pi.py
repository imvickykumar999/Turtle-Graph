import random
import matplotlib.pyplot as plt
import numpy as np

# Number of random points to generate
num_points = 10000

# Initialize counters
inside_circle = 0
x_inside = []
y_inside = []
x_outside = []
y_outside = []

# Perform the Monte Carlo simulation
for _ in range(num_points):
    x, y = random.random(), random.random()
    if x**2 + y**2 <= 1:
        inside_circle += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

# Estimate π based on the ratio of points inside the quarter-circle
estimated_pi = 4 * inside_circle / num_points

# Create a plot to visualize the simulation
plt.figure(figsize=(8, 8))
plt.scatter(x_inside, y_inside, color='blue', s=5, label='Inside Circle')
plt.scatter(x_outside, y_outside, color='red', s=5, label='Outside Circle')
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Estimation of π: {estimated_pi:.5f}')
plt.legend(loc='upper right')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
