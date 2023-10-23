import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Initialize global counters
inside_circle = 0
x_inside = []
y_inside = []
x_outside = []
y_outside = []
pi_approximations = []

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
sc = ax.scatter([], [], s=5, color='blue')
ax.set_title("Approximating Pi")

def update(frame):
    global inside_circle  # Declare inside_circle as a global variable
    x, y = random.random(), random.random()
    if x**2 + y**2 <= 1:
        inside_circle += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)
    
    pi_approximation = 4 * inside_circle / (inside_circle + len(x_outside))
    pi_approximations.append(pi_approximation)
    
    sc.set_offsets(np.column_stack([x_inside, y_inside]))
    ax.set_title(f"Approximating Pi: {pi_approximation:.8f}")

ani = FuncAnimation(fig, update, frames=range(100000), interval=20, repeat=False)  # Smaller interval for higher frame rate
plt.show()
