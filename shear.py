def shear_horizontal(x, y, sh_x):
    x_new = x + sh_x * y
    y_new = y
    return x_new, y_new

# Example
point = (2, 3)
shear_factor = 1.5
new_point = shear_horizontal(point[0], point[1], shear_factor)
print(f"Original point: {point}")
print(f"After horizontal shear: {new_point}")
