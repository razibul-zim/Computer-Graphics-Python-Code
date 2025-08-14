import matplotlib.pyplot as plt

def draw_line_midpoint(x1, y1, x2, y2):
    points = []

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
        # Vertical line case (slope is undefined)
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

    # Ensure x1 < x2 for correct plotting in this version
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1

    midpoint_points = draw_line_midpoint(x1, y1, x2, y2)
    plot_line(midpoint_points, "Mid-Point Line Drawing")
except ValueError:
    print("Please enter valid integer values for coordinates.")
