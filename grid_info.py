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


door_coords = [
    {'min': (200, 400),
     'max': (210, 400)},
    {'min': (150, 410),
     'max': (150, 420)},
    {'min': (240, 400),
     'max': (250, 400)},
    {'min': (250, 400),
     'max': (260, 400)},
    {'min': (320, 410),
     'max': (320, 420)}
]













