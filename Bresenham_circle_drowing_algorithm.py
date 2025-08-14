import matplotlib.pyplot as plt

def draw_circle_bresenham(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r

    # Separate lists for x and y values of points
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
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1

    return x_values, y_values

def plot_circle(x_values, y_values, title):
    if not x_values or not y_values:
        print("No points to plot.")
        return

    plt.figure(figsize=(6, 6))
    plt.scatter(x_values, y_values, color='blue')  # dots only (no connecting lines)

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

    x_vals, y_vals = draw_circle_bresenham(xc, yc, r)
    plot_circle(x_vals, y_vals, "Bresenham's Circle Drawing")
except ValueError:
    print("Please enter valid integer values.")