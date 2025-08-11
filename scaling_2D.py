def scale_point(x, y, Sx, Sy):
    # Scaling
    x_scaled = x * Sx
    y_scaled = y * Sy
    return x_scaled, y_scaled

# Example
x, y = 3, 4
Sx, Sy = 2, 3

x_new, y_new = scale_point(x, y, Sx, Sy)
print(f"Original point: ({x}, {y})")
print(f"Scaled point: ({x_new}, {y_new})")
