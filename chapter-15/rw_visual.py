import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk and plot the points
while True:

    walk = RandomWalk()
    walk.fill_walk()

    point_numbers = list(range(walk.num_points))

    plt.scatter(walk.x_values, walk.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(walk.x_values[-1], walk.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('Make another walk? (y/n) ')
    if keep_running.lower() == 'n':
        break
