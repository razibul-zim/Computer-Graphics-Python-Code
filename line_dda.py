import matplotlib.pyplot as plt
def drow_line(x1,y1,x2,y2):
    point=[]
    dx=x2-x1
    dy=y2-y1
    steps = max(abs(dx),abs(dy))

    if steps == 0:
        return(round(x1),round(y1))
    x_increment = dx/steps
    y_increment = dy/steps

    x =x1
    y =y1

    for _ in range(steps+1):
        point.append((round(x),round(y)))

        x += x_increment
        y += y_increment

    return point

def plot_line(point, title):
    x_values , y_values = zip(*point)
    plt.plot(x_values , y_values,marker='o')
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('y-axis')
    plt.grid(True)
    plt.savefig('dda_point.png')
    plt.show()


if __name__  == '__main__' :

    x1 , y1 = 2,3
    x2 , y2 = 9,8

    ddd_points = drow_line( x1 , y1 ,x2 , y2)
    plot_line( ddd_points , 'Digital Differential Analyzer ')






