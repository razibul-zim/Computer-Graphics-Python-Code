import math

def rotate_point(x, y, theta):
    
    x_new = x * math.cos(theta) - y * math.sin(theta)
    y_new = x * math.sin(theta) + y * math.cos(theta)
    return x_new, y_new
# Example
point = (1, 0)
angle_degrees = 90
angle_radians = math.radians(angle_degrees)

rotated_point = rotate_point(point[0], point[1], angle_radians)
print(f"Original point: {point}")
print(f"Rotated point by {angle_degrees} degrees: {rotated_point}")
