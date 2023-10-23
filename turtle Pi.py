import turtle
import random
import math

# Set up the Turtle screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Approximating Pi")

# Create a Turtle object
pi_approximation_turtle = turtle.Turtle()
pi_approximation_turtle.penup()
pi_approximation_turtle.hideturtle()

# Initialize global counters
inside_circle = 0
total_points = 0

# Function to draw the approximation
def draw_approximation():
    global inside_circle, total_points
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    total_points += 1
    distance = math.sqrt(x**2 + y**2)

    if distance <= 1:
        inside_circle += 1
        pi_approximation_turtle.color("blue")
    else:
        pi_approximation_turtle.color("red")
    
    pi_approximation_turtle.goto(x * 200, y * 200)
    pi_approximation_turtle.dot()

    # Calculate pi approximation
    pi_approximation = 4 * inside_circle / total_points

    # Update the title
    wn.title(f"Approximating Pi: {pi_approximation:.8f}")

# Function to update the approximation
def update_approximation():
    draw_approximation()
    wn.ontimer(update_approximation, 10)  # 10 millisecond delay for a faster frame rate

# Start the animation
update_approximation()

# Close the Turtle graphics window by clicking it
wn.exitonclick()
