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