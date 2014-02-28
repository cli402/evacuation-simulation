from vector import Vector
# Grid information

MAX_INT = 32767

FPS=30



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
	(12, 24, (94, 0)),	  #1  Spring, north of 5th, west sidewalk
	(10, 24, (146, 0)),	 #2  Spring, north of 5th, east sidewalk
	(12, 24, (824, 0)),	 #3  West Peachtree, north of 5th, west sidewalk
	(10, 60, (876, 0)),	 #4  West Peachtree, north of 5th, east sidewalk
	(106, 12, (0, 12)),	 #5  5th, running west, north sidewalk
	(40, 10, (106, 14)),	#6  Spring, 5th, north crosswalk
	(690, 10, (146, 14)),   #7  5th, between West Peachtree and Spring, north sidewalk
	(40, 10, (836, 14)),	#8  West Peachtree, 5th between West Peachtree and Spring, north crosswalk
	(10, 36, (96, 24)),	 #9  5th, running west, Spring, west crosswalk
	(10, 36, (146, 24)),	#10  5th, running west, Spring, east crosswalk
	(10, 36, (826, 24)),	#11  5th, between West Peachtree and Spring, West Peachtree, crosswalk
	(106, 14, (0, 60)),	 #12  5th, running west, south sidewalk
	(40, 10, (106, 60)),	#13  Spring, 5th, south crosswalk
	(210, 12, (146, 60)),   #14  5th, between West Peachtree and Spring, west side, south sidewalk
	(330, 8, (356, 60)),	#15  5th, between West Peachtree and Spring, middle, south sidewalk
	(220, 10, (596, 60)),   #16  5th, between West Peachtree and Spring, east, south sidewalk
	(40, 10, (836, 60)),	#17  West Peachtree, 5th between West Peachtree and Spring, south crosswalk
	(16, 570, (90, 60)),	#18  Spring, between Armstead and 5th, west sidewalk
	(12, 530, (146, 60)),   #19  Spring, between Armstead and 5th, east sidewalk
	(20, 260, (816, 60)),   #20  West Peachtree, between 5th and 5th, west sidewalk
	(10, 260, (876, 60)),   #21  West Peachtree, between 5th and 5th, east sidewalk
	(40, 10, (836, 310)),   #22  West Peachtree, 5th running east, north crosswalk
	(12, 10, (886, 310)),   #23  5th, running east, north sidewalk
	(10, 30, (876, 320)),   #24  5th, running east, crosswalk
	(40, 10, (836, 350)),   #25  West Peachtree, 5th running east, south crosswalk
	(12, 10, (886, 350)),   #26  5th, running east, south sidwalk
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
	(8, 360, (146, 628)),	#37  Spring, south of Armstead, east sidewalk
	(8, 360, (828, 628))	 #38  West Peachtree, south of Armstead, west sidewalk
]


# The list structure goes like this: traffic_lights[light[crosswalk_set[cell_coordinates[xmin, ymin, xmax, ymax]]]]
# There are three traffic lights, each one with two sets of crosswalks (west to east and north to south). For each
# light, west to east crosswalks are the first set, and north to south crosswalks are the second set. Within each
# crosswalk set, the cell coordinates for the "start" and "end" of each crosswalk are given. The "start" being the
# west side for west to east crosswalks, and the north side for north to south crosswalks. The start and end of
# each crosswalk requires four coordinates, xmin, ymin, xmax, ymax. These four coordinates give the area of cells
# that the start and end of each crosswalk occupy.

traffic_lights = [
	(
	[(Vector(54, 7), Vector(72, 12)), (Vector(54, 30), Vector(72, 35))],		#areas
	(69, 38),				#timming
	-1,				#initial
	),
#5th street & Spring street
	(
	[(Vector(48, 13), Vector(53, 29)), (Vector(73, 13), Vector(78,29))],			#areas
	(38, 69),
	1,
	),

	(
	[(Vector(419, 7), Vector(437, 12)), (Vector(419, 30), Vector(439, 35))],		#areas
	(45, 22),
	-1,
	),
#5th street & West Peachtree
	(
	[(Vector(413, 13), Vector(418, 29))],
	(22, 45),
	1,
	),

	(
	[(Vector(419, 155), Vector(437, 160)), (Vector(419, 175), Vector(437, 130))],
	(45, 35),
	-1,
	),
#5th running east, West Peachtree
	(
	[(Vector(438, 161), Vector(443, 174))],
	(35, 45),
	1
	),
]

#goal_coords = [
#	({'min': (0, grid[11][2][1] / person_size),
#	  'max': (0, (grid[11][2][1] + grid[11][1]) / person_size)},
#	 {'min': (0, grid[4][2][1] / person_size),
#	  'max': (0, (grid[4][2][1] + grid[4][1]) / person_size)}),
#	({'min': (grid[0][2][0] / person_size, 0),
#	  'max': ((grid[0][2][0] + grid[0][0]) / person_size, 0)},
#	 {'min': (grid[1][2][0] / person_size, 0),
#	  'max': ((grid[1][2][0] + grid[1][0]) / person_size, 0)}),
#	({'min': (grid[2][2][0] / person_size, 0),
#	  'max': ((grid[2][2][0] + grid[2][0]) / person_size, 0)},
#	 {'min': (grid[3][2][0] / person_size, 0),
#	  'max': ((grid[3][2][0] + grid[3][0]) / person_size, 0)}),
#	({'min': ((grid[22][2][0] + grid[22][0]) / person_size, grid[22][2][1] / person_size),
#	  'max': ((grid[22][2][0] + grid[22][0]) / person_size, (grid[22][2][1] + grid[22][1]) / person_size)},
#	 {'min': ((grid[25][2][0] + grid[25][0]) / person_size, grid[25][2][1] / person_size),
#	  'max': ((grid[25][2][0] + grid[25][0]) / person_size, (grid[25][2][1] + grid[25][1]) / person_size)})
#]


# 313 is the y coordinate for bottom row of cells on Armstead south sidewalk,
# given in person sized cell coordinates.
# The range for the x coordinates is 77 - 413, inclusive
# The x coordinate for spring south sidewalk is 76, the y range is 314 - 493, inclusive
# The x coordinate for west peachtree south sidewalk is 414, the y range is 314 - 493, inclusive # was 323
door_coords = [
	[[200, 313, 1, 0], [202, 313, 1, 0], [204, 313, 1, 0], [206, 313, 1, 0]],
	[[77, 313, 1, 0], [79, 313, 1, 0]],
	[[76, 492, 0, 1]],
	[[414, 492, 0, 1]],
	[[310, 313, 1, 0]],
	[[412, 313, 1, 0]]
]


























