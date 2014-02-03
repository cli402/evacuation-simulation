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
    (12, 200, (188, 0)),    #1  Spring, north of 5th, west sidewalk
    (10, 200, (240, 0)),    #2  Spring, north of 5th, east sidewalk
    (12, 200, (648, 0)),    #3  West Peachtree, north of 5th, west sidewalk
    (10, 200, (700, 0)),    #4  West Peachtree, north of 5th, east sidewalk
    (200, 12, (0, 188)),    #5  5th, running west, north sidewalk
    (40, 10, (200, 190)),   #6  Spring, 5th, north crosswalk
    (420, 10, (240, 190)),  #7  5th, between West Peachtree and Spring, north sidewalk
    (40, 10, (660, 190)),   #8  West Peachtree, 5th between West Peachtree and Spring, north crosswalk
    (10, 36, (190, 200)),   #9  5th, running west, Spring, west crosswalk
    (10, 36, (240, 200)),   #10  5th, running west, Spring, east crosswalk
    (10, 36, (650, 200)),   #11  5th, between West Peachtree and Spring, West Peachtree, crosswalk
    (200, 14, (0, 236)),    #12  5th, running west, south sidewalk
    (40, 10, (200, 236)),   #13  Spring, 5th, south crosswalk
    (120, 12, (240, 236)),  #14  5th, between West Peachtree and Spring, west side, south sidewalk
    (170, 8, (360, 236)),   #15  5th, between West Peachtree and Spring, middle, south sidewalk
    (130, 10, (530, 236)),  #16  5th, between West Peachtree and Spring, east, south sidewalk
    (40, 10, (660, 236)),   #17  West Peachtree, 5th between West Peachtree and Spring, south crosswalk
    (16, 320, (184, 236)),  #18  Spring, between Armstead and 5th, west sidewalk
    (12, 320, (240, 236)),  #19  Spring, between Armstead and 5th, east sidewalk
    (20, 200, (640, 236)),  #20  West Peachtree, between 5th and 5th, west sidewalk
    (10, 200, (700, 236)),  #21  West Peachtree, between 5th and 5th, east sidewalk
    (40, 10, (660, 426)),   #22  West Peachtree, 5th running east, north crosswalk
    (200, 10, (710, 426)),  #23  5th, running east, north sidewalk
    (10, 30, (700, 436)),   #24  5th, running east, crosswalk
    (40, 10, (660, 466)),   #25  West Peachtree, 5th running east, south crosswalk
    (200, 10, (710, 466)),  #26  5th, running east, south sidwalk
    (10, 120, (650, 436)),  #27  West Peachtree, between Armstead and 5th, west sidewalk
    (10, 120, (700, 466)),  #28  West Peachtree, between Armstead and 5th, east sidewalk
    (40, 10, (200, 546)),   #29  Spring, Armstead, north crosswalk
    (420, 10, (240, 546)),  #30  Armstead, north sidewalk
    (40, 10, (660, 546)),   #31  West Peachtree, Armstead, north crosswalk
    (10, 30, (240, 556)),   #32  Armstead, Spring, crosswalk
    (10, 30, (650, 556)),   #33  Armstead, West Peachtree, crosswalk
    (40, 10, (200, 586)),   #34  Spring, Armstead, south crosswalk
    (420, 8, (240, 586)),   #35  Armstead, south sidewalk
    (40, 10, (660, 586)),   #36  West Peachtree, Armstead, south crosswalk
]

