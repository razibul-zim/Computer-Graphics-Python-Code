import matplotlib.pyplot as plt

# Original square coordinates
A = (0, 3)
B = (3, 3)
C = (3, 0)
D = (0, 0)

# Scaling factors
sx, sy = 2, 3

# Apply scaling
A_new = (A[0] * sx, A[1] * sy)
B_new = (B[0] * sx, B[1] * sy)
C_new = (C[0] * sx, C[1] * sy)
D_new = (D[0] * sx, D[1] * sy)

# Prepare coordinates for plotting
original_x = [A[0], B[0], C[0], D[0], A[0]]
original_y = [A[1], B[1], C[1], D[1], A[1]]

scaled_x = [A_new[0], B_new[0], C_new[0], D_new[0], A_new[0]]
scaled_y = [A_new[1], B_new[1], C_new[1], D_new[1], A_new[1]]

# Plotting
plt.figure(figsize=(6,6))
plt.plot(original_x, original_y, 'b-o', label='Original Square')
plt.plot(scaled_x, scaled_y, 'r-o', label='Scaled Square')

plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.title('2D Scaling of a Square')
plt.axis('equal')
plt.show()

# Print new coordinates
print("New coordinates after scaling:")
print(f"A' = {A_new}")
print(f"B' = {B_new}")
print(f"C' = {C_new}")
print(f"D' = {D_new}")
