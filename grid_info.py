# Grid information




# Define grid sizes. Values given in pixels
pixels_per_foot = 1.6042094455852156057494866529774
person_size = 2
grid_size = (1350, 950)
tile_size = int(person_size * pixels_per_foot)
x_range = int(grid_size[0] / tile_size)
y_range = int(grid_size[1] / tile_size)