# Grid information




# Define grid sizes. Values given in pixels
pixels_per_foot = 1.6042094455852156057494866529774
#pixels_per_foot = 3
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
    (12, 24, (94, 0)),    #1  Spring, north of 5th, west sidewalk
    (10, 24, (146, 0)),    #2  Spring, north of 5th, east sidewalk
    (12, 24, (824, 0)),    #3  West Peachtree, north of 5th, west sidewalk
    (10, 60, (876, 0)),    #4  West Peachtree, north of 5th, east sidewalk
    (106, 12, (0, 12)),    #5  5th, running west, north sidewalk
    (40, 10, (106, 14)),   #6  Spring, 5th, north crosswalk
    (690, 10, (146, 14)),  #7  5th, between West Peachtree and Spring, north sidewalk
    (40, 10, (836, 14)),   #8  West Peachtree, 5th between West Peachtree and Spring, north crosswalk
    (10, 36, (96, 24)),   #9  5th, running west, Spring, west crosswalk
    (10, 36, (146, 24)),   #10  5th, running west, Spring, east crosswalk
    (10, 36, (826, 24)),   #11  5th, between West Peachtree and Spring, West Peachtree, crosswalk
    (106, 14, (0, 60)),    #12  5th, running west, south sidewalk
    (40, 10, (106, 60)),   #13  Spring, 5th, south crosswalk
    (210, 12, (146, 60)),  #14  5th, between West Peachtree and Spring, west side, south sidewalk
    (330, 8, (356, 60)),   #15  5th, between West Peachtree and Spring, middle, south sidewalk
    (220, 10, (596, 60)),  #16  5th, between West Peachtree and Spring, east, south sidewalk
    (40, 10, (836, 60)),   #17  West Peachtree, 5th between West Peachtree and Spring, south crosswalk
    (16, 570, (90, 60)),  #18  Spring, between Armstead and 5th, west sidewalk
    (12, 530, (146, 60)),  #19  Spring, between Armstead and 5th, east sidewalk
    (20, 260, (816, 60)),  #20  West Peachtree, between 5th and 5th, west sidewalk
    (10, 260, (876, 60)),  #21  West Peachtree, between 5th and 5th, east sidewalk
    (40, 10, (836, 310)),   #22  West Peachtree, 5th running east, north crosswalk
    (12, 10, (886, 310)),  #23  5th, running east, north sidewalk
    (10, 30, (876, 320)),   #24  5th, running east, crosswalk
    (40, 10, (836, 350)),   #25  West Peachtree, 5th running east, south crosswalk
    (12, 10, (886, 350)),  #26  5th, running east, south sidwalk
    (10, 260, (826, 320)),  #27  West Peachtree, between Armstead and 5th, west sidewalk
    (10, 280, (876, 350)),  #28  West Peachtree, between Armstead and 5th, east sidewalk
    (40, 10, (106, 580)),   #29  Spring, Armstead, north crosswalk
    (690, 10, (146, 580)),  #30  Armstead, north sidewalk
    (40, 10, (836, 580)),   #31  West Peachtree, Armstead, north crosswalk
    (10, 30, (146, 590)),   #32  Armstead, Spring, crosswalk
    (10, 30, (826, 590)),   #33  Armstead, West Peachtree, crosswalk
    (40, 10, (106, 620)),   #34  Spring, Armstead, south crosswalk
    (690, 8, (146, 620)),   #35  Armstead, south sidewalk
    (40, 10, (836, 620)),   #36  West Peachtree, Armstead, south crosswalk
]


# The list structure goes like this: traffic_lights[light[crosswalk_set[cell_coordinates[xmin, ymin, xmax, ymax]]]]
# There are three traffic lights, each one with two sets of crosswalks (west to east and north to south). For each
# light, west to east crosswalks are the first set, and north to south crosswalks are the second set. Within each
# crosswalk set, the cell coordinates for the "start" and "end" of each crosswalk are given. The "start" being the
# west side for west to east crosswalks, and the north side for north to south crosswalks. The start and end of
# each crosswalk requires four coordinates, xmin, ymin, xmax, ymax. These four coordinates give the area of cells
# that the start and end of each crosswalk occupy.
traffic_lights = [
    [[[106, 14, 106, 24], [146, 14, 146, 24], [106, 60, 106, 70], [146, 60, 146, 70]],
     [[96, 24, 106, 24], [96, 60, 106, 60], [146, 24, 156, 24], [146, 60, 156, 60]]],
    [[[836, 14, 836, 24], [876, 14, 876, 24], [836, 60, 836, 70], [876, 60, 876, 70]],
     [[826, 24, 836, 24], [826, 60, 836, 60]]],
    [[[836, 310, 836, 320], [876, 310, 876, 320], [836, 350, 836, 360], [876, 350, 876, 360]],
     [[876, 320, 886, 320], [876, 350, 886, 350]]]
]

for light_set in traffic_lights:
    for light in light_set:
        for coords in light:
            coords[0] /= person_size
            coords[1] /= person_size
            coords[2] /= person_size
            coords[3] /= person_size


goal_coords = [
    ({'min': (0, grid[11][2][1] / person_size),
      'max': (0, (grid[11][2][1] + grid[11][1]) / person_size)},
     {'min': (0, grid[4][2][1] / person_size),
      'max': (0, (grid[4][2][1] + grid[4][1]) / person_size)}),
    ({'min': (grid[0][2][0] / person_size, 0),
      'max': ((grid[0][2][0] + grid[0][0]) / person_size, 0)},
     {'min': (grid[1][2][0] / person_size, 0),
      'max': ((grid[1][2][0] + grid[1][0]) / person_size, 0)}),
    ({'min': (grid[2][2][0] / person_size, 0),
      'max': ((grid[2][2][0] + grid[2][0]) / person_size, 0)},
     {'min': (grid[3][2][0] / person_size, 0),
      'max': ((grid[3][2][0] + grid[3][0]) / person_size, 0)}),
    ({'min': ((grid[22][2][0] + grid[22][0]) / person_size, grid[22][2][1] / person_size),
      'max': ((grid[22][2][0] + grid[22][0]) / person_size, (grid[22][2][1] + grid[22][1]) / person_size)},
     {'min': ((grid[25][2][0] + grid[25][0]) / person_size, grid[25][2][1] / person_size),
      'max': ((grid[25][2][0] + grid[25][0]) / person_size, (grid[25][2][1] + grid[25][1]) / person_size)})
]


# 313 is the y coordinate for bottom row of cells on Armstead south sidewalk,
# given in person sized cell coordinates.
# The range for the x coordinates is 73 - 417, inclusive
door_coords = [
    {'min': (74, 313),
     'max': (84, 313)},
    {'min': (100, 313),
     'max': (110, 313)},
    {'min': (250, 313),
     'max': (260, 313)},
    {'min': (310, 313),
     'max': (320, 313)},
    {'min': (400, 313),
     'max': (410, 313)}
]





























