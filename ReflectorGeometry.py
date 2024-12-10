import math
import numpy as np
from scipy.integrate import quad

# === Initializations and Definitions ===

#M1 is the point that the line crosses that also crosses through A, B
#M2 is the point that the line crosses that also crosses through A, B and B on plane A
#M3 is the point that the line crosses that also crosses through A, B and B on plane B

# Dish-related parameters
dish_diameter = 800
dish_focal_length = 400


length_c = dish_diameter * math.sin(math.pi / 12)

# Parabola parameters
A_depth = (dish_diameter / 2) ** 2 / (4 * dish_focal_length)
A_scalingfactor = A_depth / (dish_diameter / 2) ** 2

# Newton-Raphson parameters
initial_guess = 100
tolerance = 1e-10
max_iterations = 100

# === Function Definitions ===
# Function and derivative of the parabola
def parabola_function_and_derivative(x, scalingfactor, Mx, My):
    # Parabola function
    f_x = -(2*scalingfactor**2 * x**3) + (2 * scalingfactor * My * x) - x + Mx
    # Derivative of the parabola function
    df_x = -(2*scalingfactor**2 * 3 * x**2) + (2 * scalingfactor * My * 1) - 1
    return f_x, df_x

# Generalized Newton-Raphson method for finding roots
def newton_raphson(initial_guess, tolerance, max_iterations, scalingfactor, Mx, My):
    x = initial_guess
    for _ in range(max_iterations):
        f_x, df_x = parabola_function_and_derivative(x, scalingfactor, Mx, My)
        x_new = x - f_x / df_x
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    return None

# Arc length calculation for a parabola
def parabola_arc_length(parabola_depth, diameter):
    b = diameter
    sqrt_term = math.sqrt(b**2 + 16 * parabola_depth**2)
    arc_length = 0.5 * sqrt_term + (b**2 / (8 * parabola_depth)) * math.log((4 * parabola_depth + sqrt_term) / b)
    return arc_length


def A_df(x):
    return (A_scalingfactor*2) * x

def B_df(x):
    return (B_scalingfactor*2) * x

#Calculate the arc length of a curve over the interval [a, b].
def calculate_arc_length_with_interval(f_prime, a, b): 
    # Define the integrand function
    def integrand(x):
        return np.sqrt(1 + (f_prime(x))**2)
    
    # Perform the integration
    arc_length, _ = quad(integrand, a, b)
    return arc_length

# Calculate the side length given an angle (law of cosines)
def calculate_side_length(a, b, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    return math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angle_radians))


# === Calculations ===

# Calculate result for Parabola A
M1x = dish_diameter / 4
M1y = A_depth
Q1x = newton_raphson(initial_guess, tolerance, max_iterations, A_scalingfactor, M1x, M1y)
Q1y = A_scalingfactor * Q1x**2
arc_length_A = parabola_arc_length(A_depth, dish_diameter)

# Calculate parameters for Parabola B
B_diameter = calculate_side_length(dish_diameter / 2, dish_diameter / 2, 360 / 12 * 4)
B_depth = calculate_side_length(A_depth - Q1y, Q1x - M1x, 90)
B_arclength = parabola_arc_length(B_depth, B_diameter)
B_scalingfactor = B_depth/(B_diameter / 2)** 2

# Calculate result for Parabola B
M2x = (dish_diameter / 2) * (math.sin(math.radians(360 / 12)) / math.sin(math.radians(360 / 12 * 2)))
M2y = A_depth
Q2x = newton_raphson(initial_guess, tolerance, max_iterations, A_scalingfactor, M2x, M2y)
Q2y = A_scalingfactor * Q2x**2

M3x = M2x/2
M3y = B_depth
Q3x =  newton_raphson(initial_guess, tolerance, max_iterations, B_scalingfactor, M3x, M3y)
Q3y = B_scalingfactor * Q3x**2

# Additional length calculations for segments
length_A2 = parabola_arc_length(A_depth - Q1y, Q1x * 2) / 2


segment_A1 = calculate_arc_length_with_interval(A_df, 0, Q2x)
segment_A2 = (arc_length_A-(segment_A1*2))/2
segment_B1 = (calculate_arc_length_with_interval(B_df, 0, Q3x))*2
segment_B2 = (B_arclength-(segment_B1))/2


# === Output Results ===

print("\nGiven input:")
print("Reflector diameter: " ,dish_diameter)
print("Reflector focal length: " ,dish_focal_length)

print("\nResults:")

print("\nParabola A:")
print(f"Dish Depth: {A_depth}")
print(f"Function: f(x) = {A_scalingfactor} * x^2")
print(f"M1: P({M1x} | {A_depth})")
print(f"Crossing Point of A,B on plane of parabola A (Origin of Segment B): P({Q1x} | {Q1y})")
print(f"Arc Length: {arc_length_A}")

print("\nParabola B:")
print(f"Parabola Depth: {B_depth}")
print(f"Function: f(x) = {B_scalingfactor} * x^2")
print(f"Parabola Diameter: {B_diameter}")
print(f"M2 (on parabola A plane): P({M2x} | {A_depth})")
print(f"Crossing Point of A,B,B on plane of parabola A: P({Q2x} | {Q2y})")
print(f"M3 (on parabola B plane): P({M3x} | {M3y})")
print(f"Crossing Point of A,B,B on plane of parabola B: P({Q3x} | {Q3y})")
print(f"Arc Length: {B_arclength}")


print("\nSegment lengths:")
print("Length of Segment A1:", segment_A1)
print("Length of Segment A2:", segment_A2)



print("Length of Segment B1:", segment_B1)
print("Length of Segment B2:", segment_B2)

print("\nLength of C:",length_c )

