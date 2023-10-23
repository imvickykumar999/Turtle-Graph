import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parameters for the helix
theta = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
z = np.linspace(-2, 2, 1000)
r = z
x = r * np.sin(theta)
y = r * np.cos(theta)

# Create the initial helix line
line, = ax.plot(x, y, z, lw=2)

# Function to update the helix
def update(frame):
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    return line,

# Create an animation for the helix with a faster frame rate
ani = FuncAnimation(fig, update, frames=range(1000), interval=10, blit=True)  # Adjust the interval for desired frame rate

# Show the animation
plt.show()
