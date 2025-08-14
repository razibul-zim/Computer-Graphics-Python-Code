# Computer Graphics Algorithms and Transformations in Python

---

## 1. DDA Algorithm

```python
import matplotlib.pyplot as plt

def draw_line_DDA(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))

    x_increment = dx / steps
    y_increment = dy / steps

    x, y = x1, y1

    for _ in range(int(steps) + 1):  # include last point
        points.append((round(x), round(y)))
        x += x_increment
        y += y_increment

    return points

def plot_line(points, title):
    x_values, y_values = zip(*points)
    plt.plot(x_values, y_values, marker='o')

    # Annotate each point
    for (x, y) in points:
        plt.text(x + 0.1, y + 0.1, f"({x},{y})", fontsize=9, color='red')

    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

# User input
try:
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    dda_points = draw_line_DDA(x1, y1, x2, y2)
    plot_line(dda_points, 'DDA Line Drawing')
except ValueError:
    print("Please enter valid integer coordinates.")
```

## 2. Bresenham's Line Drawing Algorithm

```Python
import matplotlib.pyplot as plt

def draw_line_Bresenham(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1

    x, y = x1, y1
    points.append((x, y))
    p = 2 * dy - dx

    for _ in range(dx):
        x += 1
        if p < 0:
            p = p + 2 * dy
        else:
            p = p + 2 * dy - 2 * dx
            y += 1
        points.append((x, y))

    return points

def plot_line(points, title):
    x_values, y_values = zip(*points)
    plt.plot(x_values, y_values, marker='o')
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

# User input
try:
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    bresenham_points = draw_line_Bresenham(x1, y1, x2, y2)
    plot_line(bresenham_points, "Bresenham's Line Drawing")
except ValueError:
    print("Please enter valid integer values for coordinates.")
```

## 3. Midpoint Line Drawing Algorithm

```python
import matplotlib.pyplot as plt

def draw_line_midpoint(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:  # Vertical line
        for y in range(y1, y2 + 1):
            points.append((x1, y))
        return points

    if abs(dy) > abs(dx):
        print("This basic version only supports slope between 0 and 1.")
        return []

    x, y = x1, y1
    d = dy - (dx / 2)
    points.append((x, y))

    while x < x2:
        x += 1
        if d < 0:
            d = d + dy
        else:
            y += 1
            d = d + dy - dx
        points.append((x, y))

    return points

def plot_line(points, title):
    if not points:
        print("No points to plot.")
        return
    x_values, y_values = zip(*points)
    plt.plot(x_values, y_values, marker='o')
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

# User input
try:
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1

    midpoint_points = draw_line_midpoint(x1, y1, x2, y2)
    plot_line(midpoint_points, "Mid-Point Line Drawing")
except ValueError:
    print("Please enter valid integer values for coordinates.")
```

## 4. Bresenham's Circle Drawing Algorithm

```python
import matplotlib.pyplot as plt

def draw_circle_bresenham(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    x_values, y_values = []

    def plot_symmetric_points(xc, yc, x, y):
        coords = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ]
        for px, py in coords:
            x_values.append(px)
            y_values.append(py)

    while x <= y:
        plot_symmetric_points(xc, yc, x, y)
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1

    return x_values, y_values

def plot_circle(x_values, y_values, title):
    plt.figure(figsize=(6, 6))
    plt.scatter(x_values, y_values, color='blue')
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# User input
try:
    xc = int(input("Enter center x: "))
    yc = int(input("Enter center y: "))
    r = int(input("Enter radius: "))

    x_vals, y_vals = draw_circle_bresenham(xc, yc, r)
    plot_circle(x_vals, y_vals, "Bresenham's Circle Drawing")
except ValueError:
    print("Please enter valid integer values.")
```

---

## 5. Midpoint Circle Drawing Algorithm

```python
import matplotlib.pyplot as plt

def draw_circle_midpoint(xc, yc, r):
    x = 0
    y = r
    d = 1 - r  # Initial decision parameter

    x_values = []
    y_values = []

    def plot_symmetric_points(xc, yc, x, y):
        coords = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ]
        for px, py in coords:
            x_values.append(px)
            y_values.append(py)

    while x <= y:
        plot_symmetric_points(xc, yc, x, y)
        if d < 0:
            d += 2 * x + 1       # East
        else:
            d += 2 * (x - y) + 1 # South-East
            y -= 1
        x += 1

    return x_values, y_values

def plot_circle(x_values, y_values, title):
    if not x_values or not y_values:
        print("No points to plot.")
        return

    plt.figure(figsize=(6, 6))
    plt.scatter(x_values, y_values, color='blue')  # blue dots only

    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks(range(min(x_values) - 1, max(x_values) + 2))
    plt.yticks(range(min(y_values) - 1, max(y_values) + 2))
    plt.show()

# User input
try:
    xc = int(input("Enter center x (xc): "))
    yc = int(input("Enter center y (yc): "))
    r = int(input("Enter radius (r): "))

    x_vals, y_vals = draw_circle_midpoint(xc, yc, r)
    plot_circle(x_vals, y_vals, "Midpoint Circle Drawing")
except ValueError:
    print("Please enter valid integer values.")

```

## 6. Translation

```python
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

plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.title('2D Translation of a Square')
plt.axis('equal')
plt.show()

print("New coordinates after translation:")
print(f"A' = {A_new}")
print(f"B' = {B_new}")
print(f"C' = {C_new}")
print(f"D' = {D_new}")

```

## 7. Scaling

```python
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

print("New coordinates after scaling:")
print(f"A' = {A_new}")
print(f"B' = {B_new}")
print(f"C' = {C_new}")
print(f"D' = {D_new}")

```

## 8. Rotation

```python
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

print("New coordinates after rotation:")
print(f"P1' = {P1_new}")
print(f"P2' = {P2_new}")
print(f"P3' = {P3_new}")

```

## 9. Reflection

```python
import matplotlib.pyplot as plt

# Original triangle points
A = (3, 4)
B = (6, 4)
C = (5, 6)

# Reflection formulas
def reflect_x(x, y):
    return x, -y

def reflect_y(x, y):
    return -x, y

# Apply reflections
A_x = reflect_x(*A)
B_x = reflect_x(*B)
C_x = reflect_x(*C)

A_y = reflect_y(*A)
B_y = reflect_y(*B)
C_y = reflect_y(*C)

# Prepare coordinates for plotting
orig_x = [A[0], B[0], C[0], A[0]]
orig_y = [A[1], B[1], C[1], A[1]]

xaxis_x = [A_x[0], B_x[0], C_x[0], A_x[0]]
xaxis_y = [A_x[1], B_x[1], C_x[1], A_x[1]]

yaxis_x = [A_y[0], B_y[0], C_y[0], A_y[0]]
yaxis_y = [A_y[1], B_y[1], C_y[1], A_y[1]]

# Plotting
plt.figure(figsize=(7,7))
plt.plot(orig_x, orig_y, 'b-o', label='Original Triangle')
plt.plot(xaxis_x, xaxis_y, 'r-o', label='Reflected along X-axis')
plt.plot(yaxis_x, yaxis_y, 'g-o', label='Reflected along Y-axis')

plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.title('Reflection of a Triangle along X-axis and Y-axis')
plt.axis('equal')
plt.show()

print("Reflection along X-axis:")
print(f"A' = {A_x}")
print(f"B' = {B_x}")
print(f"C' = {C_x}")

print("\nReflection along Y-axis:")
print(f"A'' = {A_y}")
print(f"B'' = {B_y}")
print(f"C'' = {C_y}")

```

## 10. Shearing

```python
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
plt.plot([O[0], B[0], A[0], O[0]], [O[1], B[1], A[1], O[1]], 'bo-', label='Original')
plt.plot([O_x[0], B_x[0], A_x[0], O_x[0]], [O_x[1], B_x[1], A_x[1], O_x[1]], 'ro-', label='Sheared in X-axis')
plt.title("Shearing in X-axis (Shx = 2)")
plt.axis('equal')
plt.grid(True)
plt.legend()

# Plot for Y-axis Shearing
plt.subplot(1, 2, 2)
plt.plot([O[0], B[0], A[0], O[0]], [O[1], B[1], A[1], O[1]], 'bo-', label='Original')
plt.plot([O_y[0], B_y[0], A_y[0], O_y[0]], [O_y[1], B_y[1], A_y[1], O_y[1]], 'ro-', label='Sheared in Y-axis')
plt.title("Shearing in Y-axis (Shy = 2)")
plt.axis('equal')
plt.grid(True)
plt.legend()

plt.show()

print("Shearing in X-axis:")
print(f"A' = {A_x}")
print(f"B' = {B_x}")
print(f"O' = {O_x}")

print("\nShearing in Y-axis:")
print(f"A' = {A_y}")
print(f"B' = {B_y}")
print(f"O' = {O_y}")

```
