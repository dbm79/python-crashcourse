import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk and plot the points
walk = RandomWalk()
walk.fill_walk()

plt.scatter(walk.x_values, walk.y_values, s=10)
plt.show()
