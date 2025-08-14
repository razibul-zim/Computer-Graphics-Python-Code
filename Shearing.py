
import matplotlib.pyplot as plt

# Original triangle coordinates
O = (0, 0)
B = (1, 0)
A = (1, 1)

# Shearing in X-axis (Shx = 2)
Shx = 2
A_x = (A[0] + Shx * A[1], A[1])
B_x = (B[0] + Shx * B[1], B[1])
O_x = (O[0] + Shx * O[1], O[1])

# Shearing in Y-axis (Shy = 2)
Shy = 2
A_y = (A[0], A[1] + Shy * A[0])
B_y = (B[0], B[1] + Shy * B[0])
O_y = (O[0], O[1] + Shy * O[0])

# Plot for X-axis Shearing
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
# Original
plt.plot([O[0], B[0], A[0], O[0]], [O[1], B[1], A[1], O[1]], 'bo-', label='Original')
# Sheared
plt.plot([O_x[0], B_x[0], A_x[0], O_x[0]], [O_x[1], B_x[1], A_x[1], O_x[1]], 'ro-', label='Sheared in X-axis')
plt.title("Shearing in X-axis (Shx = 2)")
plt.axis('equal')
plt.grid(True)
plt.legend()

# Plot for Y-axis Shearing
plt.subplot(1, 2, 2)
# Original
plt.plot([O[0], B[0], A[0], O[0]], [O[1], B[1], A[1], O[1]], 'bo-', label='Original')
# Sheared
plt.plot([O_y[0], B_y[0], A_y[0], O_y[0]], [O_y[1], B_y[1], A_y[1], O_y[1]], 'ro-', label='Sheared in Y-axis')
plt.title("Shearing in Y-axis (Shy = 2)")
plt.axis('equal')
plt.grid(True)
plt.legend()

plt.show()

# Print new coordinates
print("Shearing in X-axis:")
print(f"A' = {A_x}")
print(f"B' = {B_x}")
print(f"O' = {O_x}")

print("\nShearing in Y-axis:")
print(f"A' = {A_y}")
print(f"B' = {B_y}")
print(f"O' = {O_y}")