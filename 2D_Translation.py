import matplotlib.pyplot as plt

# Original coordinates
A = (0, 3)
B = (3, 3)
C = (3, 0)
D = (0, 0)

# Translation distances
tx, ty = 1, 1

# Apply translation
A_new = (A[0] + tx, A[1] + ty)
B_new = (B[0] + tx, B[1] + ty)
C_new = (C[0] + tx, C[1] + ty)
D_new = (D[0] + tx, D[1] + ty)

# Prepare coordinates for plotting
original_x = [A[0], B[0], C[0], D[0], A[0]]
original_y = [A[1], B[1], C[1], D[1], A[1]]

translated_x = [A_new[0], B_new[0], C_new[0], D_new[0], A_new[0]]
translated_y = [A_new[1], B_new[1], C_new[1], D_new[1], A_new[1]]

# Plotting
plt.figure(figsize=(6,6))
plt.plot(original_x, original_y, 'b-o', label='Original Square')
plt.plot(translated_x, translated_y, 'r-o', label='Translated Square')

# Add point labels
points_original = ['A', 'B', 'C', 'D']
points_new = ["A'", "B'", "C'", "D'"]

for i, txt in enumerate(points_original):
    plt.text(original_x[i]-0.2, original_y[i]+0.2, txt, fontsize=10, color='blue')

for i, txt in enumerate(points_new):
    plt.text(translated_x[i]-0.2, translated_y[i]+0.2, txt, fontsize=10, color='red')

# Formatting
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.title('2D Translation of a Square')
plt.axis('equal')
plt.show()

# Output new coordinates
print("New coordinates after translation:")
print(f"A' = {A_new}")
print(f"B' = {B_new}")
print(f"C' = {C_new}")
print(f"D' = {D_new}")