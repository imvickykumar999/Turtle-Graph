import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the ODE (e.g., dy/dx = -k * y)
def model(y, t):
    k = 0.1
    dydt = -k * y
    return dydt

# Initial condition
y0 = 5

# Time points
t = np.linspace(0, 20, 100)

# Solve the ODE
y = odeint(model, y0, t)

# Create a plot
plt.figure()
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Euler Equation Solution')
plt.grid(True)
plt.show()
