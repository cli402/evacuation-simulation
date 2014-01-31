# Grid information


import random
import time


# Define grid sizes. Values given in pixels
pixels_per_foot = 1.6042094455852156057494866529774
person_size = 2
grid_size = (1350, 950)
tile_size = int(person_size * pixels_per_foot)
x_range = int(grid_size[0] / tile_size)
y_range = int(grid_size[1] / tile_size)

# random weight
weight = 100


# Seed the random number generator
random.seed(int(time.time()))

# Create a weighted grid of random 1's and 0's
def update_grid():
    grid = [[0 if random.randint(1, 100) < weight else 1 for i in xrange(x_range)] for j in xrange(y_range)]
    return grid