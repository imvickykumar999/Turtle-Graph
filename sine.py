import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 1000)
line, = ax.plot(x, np.sin(x))

# Function to update the sine curve
def update(frame):
    line.set_ydata(np.sin(x + 0.1 * frame))
    return line,

# Create an animation with a faster frame rate (e.g., 30 frames per second)
ani = FuncAnimation(fig, update, frames=range(200), interval=33.33, blit=True)  # 1000ms / 30fps = 33.33ms per frame

# Show the animation
plt.show()
