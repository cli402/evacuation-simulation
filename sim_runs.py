import grid_info
import main
import time
import random


coord_list = [
    [105, 313, 1, 0],
    [159, 313, 1, 0],
    [213, 313, 1, 0],
    [267, 313, 1, 0],
    [312, 313, 1, 0],
    [375, 313, 1, 0],
    [76, 334, 0, 1],
    [76, 362, 0, 1],
    [76, 390, 0, 1],
    [76, 418, 0, 1],
    [76, 446, 0, 1],
    [76, 474, 0, 1],
    [414, 334, 0, 1],
    [414, 362, 0, 1],
    [414, 390, 0, 1],
    [414, 418, 0, 1],
    [414, 446, 0, 1],
    [414, 474, 0, 1]
]


door_pos = [
    [8, 7, 6, 9, 10, 11],
    [14, 13, 12, 15, 16, 17],
    [2, 3, 4, 5, 0, 1],
    [5, 0, 11, 7, 13, 17],
    [3, 2, 6, 11, 12, 17],
    [0, 5, 2, 3, 11, 17],
    [13, 16, 0, 2, 6, 9],
    [7, 10, 5, 12, 3, 16],
    [13, 0, 6, 4, 11, 17],
    [13, 8, 0, 5, 2, 3],
    random.sample(xrange(18), 6),
    random.sample(xrange(18), 6),
    random.sample(xrange(18), 6),
    random.sample(xrange(18), 6),
    random.sample(xrange(18), 6),
    random.sample(xrange(18), 6),
    random.sample(xrange(18), 6),
    random.sample(xrange(18), 6),
    random.sample(xrange(18), 6),
    random.sample(xrange(18), 6)
]


#door_coords = [
#    [[77, 313, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
#    [[97, 313, 1, 0], [0, 0, 1, 0]],
#    [[117, 313, 1, 0]],
#    [[137, 313, 1, 0]],
#    [[157, 313, 1, 0]],
#    [[177, 313, 1, 0]]
#]

result_file = 'timestep_results.csv'

def sim_runs():
    seed = int(time.time())

    with open(result_file, 'w') as fo:
        fo.write('Time_Steps,4_Door,2_Door,1_Door,1_Door,1_Door,1_Door\n')
        
    # 313 is the y coordinate for bottom row of cells on Armstead south sidewalk,
    # given in person sized cell coordinates.
    # The range for the x coordinates is 77 - 413, inclusive
    # The x coordinate for spring south sidewalk is 76, the y range is 314 - 493, inclusive
    # The x coordinate for west peachtree south sidewalk is 414, the y range is 314 - 493, inclusive # was 323
    for pos in door_pos:
        temp_list = [
            [list(coord_list[pos[0]]), list(coord_list[pos[0]]), list(coord_list[pos[0]]), list(coord_list[pos[0]])],
            [list(coord_list[pos[1]]), list(coord_list[pos[1]])],
            [list(coord_list[pos[2]])],
            [list(coord_list[pos[3]])],
            [list(coord_list[pos[4]])],
            [list(coord_list[pos[5]])]
        ]

        door_coords = temp_list

        #setup locations for 4 door and 2 door, they will always be next to each other
        coord = 0 if door_coords[0][0][2] else 1
        for i in range(1, 4):
            door_coords[0][i][coord] = door_coords[0][i - 1][coord] + 2
            door_coords[0][i][coord^1] = door_coords[0][i - 1][coord^1]

        coord = 0 if door_coords[1][0][2] else 1
        door_coords[1][1][coord] = door_coords[1][0][coord] + 2
        door_coords[1][1][coord^1] = door_coords[1][0][coord^1]
    
        #print door_coords
        #for i in xrange(7):
        #    for doorlist in door_coords[1:]:
        #        coord = 0 if doorlist[0][2] else 1
        #        for door in doorlist:
        #            door[coord] += 20
             
        # run simulations        
        result = main.run_simulation(door_coords, seed)

        with open('timestep_results.csv', 'a') as fo:
            fo.write('%d,%d,%d,%d,%d,%d,%d\n'%(result, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5]))
            
        #print "Time steps: %d"%(result)



if __name__ == '__main__':
    sim_runs()







