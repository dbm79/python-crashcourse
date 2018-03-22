import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk and plot the points
while True:

    walk = RandomWalk()
    walk.fill_walk()

    point_numbers = list(range(walk.num_points))

    plt.scatter(walk.x_values, walk.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors=None, s=15)
    plt.show()

    keep_running = input('Make another walk? (y/n) ')
    if keep_running.lower() == 'n':
        break
