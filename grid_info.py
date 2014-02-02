# Grid information




# Define grid sizes. Values given in pixels
pixels_per_foot = 1.6042094455852156057494866529774
person_size = 2  # this is NOT pixels, this is feet
grid_size = (1350, 950)
tile_size = int(person_size * pixels_per_foot)
x_range = int(grid_size[0] / tile_size)
y_range = int(grid_size[1] / tile_size)


# setup the grid (length, width, (start_x, start_y))
# length is x directon, width is y. Dimensions in feet
# start_x is x coord where to start building grid section, dimensions in feet
# start_x is y coord where to start building grid section, dimensions in feet
grid = [
    (12, 200), #Spring, north of 5th, west sidewalk
    (10, 200), #Spring, north of 5th, east sidewalk
    (12, 200), #West Peachtree, north of 5th, west sidewalk
    (10, 200), #West Peachtree, north of 5th, east sidewalk
    (200, 12, (0, 188)), #5th, running west, north sidewalk
    (40, 10), #Spring, 5th, north crosswalk
    (420, 10), #5th, between West Peachtree and Spring, north sidewalk
    (40, 10), #West Peachtree, 5th between West Peachtree and Spring, north crosswalk
    (10, 36), #5th, running west, Spring, west crosswalk
    (10, 36), #5th, running west, Spring, east crosswalk
    (10, 36), #5th, between West Peachtree and Spring, West Peachtree, crosswalk
    (200, 14), #5th, running west, south sidewalk
    (40, 10), #Spring, 5th, south crosswalk
    (120, 12), #5th, between West Peachtree and Spring, west side, south sidewalk
    (170, 8), #5th, between West Peachtree and Spring, middle, south sidewalk
    (130, 10), #5th, between West Peachtree and Spring, east, south sidewalk
    (40, 10) #West Peachtree, 5th between West Peachtree and Spring, south crosswalk
    (16, 320), #Spring, between Armstead and 5th, west sidewalk
    (12, 320), #Spring, between Armstead and 5th, east sidewalk
    (20, 200), #West Peachtree, between 5th and 5th, west sidewalk
    (10, 200), #West Peachtree, between 5th and 5th, east sidewalk
    (40, 10), #West Peachtree, 5th running east, north crosswalk
    (200, 10), #5th, running east, north sidewalk
    (10, 30), #5th, running east, crosswalk
    (40, 10), #West Peachtree, 5th running east, south crosswalk
    (200, 10), #5th, running east, south sidwalk
    (10, 120), #West Peachtree, between Armstead and 5th, west sidewalk
    (10, 120), #West Peachtree, between Armstead and 5th, east sidewalk
    (40, 10), #Spring, Armstead, north crosswalk
    (420, 10), #Armstead, north sidewalk
    (40, 10), #West Peachtree, Armstead, north crosswalk
    (10, 30), #Armstead, Spring, crosswalk
    (10, 30), #Armstead, West Peachtree, crosswalk
    (40, 10), #Spring, Armstead, south crosswalk
    (420, 8), #Armstead, south sidewalk
    (40, 10), #West Peachtree, Armstead, south crosswalk
]

