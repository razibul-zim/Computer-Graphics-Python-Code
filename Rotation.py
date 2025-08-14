import matplotlib.pyplot as plt

# Original triangle coordinates
P1 = (0, 0)
P2 = (1, 0)
P3 = (1, 1)

# Rotation 90° anticlockwise: (x', y') = (-y, x)
def rotate_90_ccw(x, y):
    return -y, x

# Apply rotation
P1_new = rotate_90_ccw(*P1)
P2_new = rotate_90_ccw(*P2)
P3_new = rotate_90_ccw(*P3)

# Prepare for plotting
orig_x = [P1[0], P2[0], P3[0], P1[0]]
orig_y = [P1[1], P2[1], P3[1], P1[1]]

rot_x = [P1_new[0], P2_new[0], P3_new[0], P1_new[0]]
rot_y = [P1_new[1], P2_new[1], P3_new[1], P1_new[1]]

# Plotting
plt.figure(figsize=(6,6))
plt.plot(orig_x, orig_y, 'b-o', label='Original Triangle')
plt.plot(rot_x, rot_y, 'r-o', label='Rotated Triangle (90° CCW)')

plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.title('Rotation of a Triangle (90° Anticlockwise)')
plt.axis('equal')
plt.show()

# Print new coordinates
print("New coordinates after rotation:")
print(f"P1' = {P1_new}")
print(f"P2' = {P2_new}")
print(f"P3' = {P3_new}")
