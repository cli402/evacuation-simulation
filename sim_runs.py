import grid_info
import main
import time


def sim_runs():
    seed = int(time.time())

    # 313 is the y coordinate for bottom row of cells on Armstead south sidewalk,
    # given in person sized cell coordinates.
    # The range for the x coordinates is 77 - 413, inclusive
    # The x coordinate for spring south sidewalk is 76, the y range is 314 - 493, inclusive
    # The x coordinate for west peachtree south sidewalk is 414, the y range is 314 - 493, inclusive # was 323
    door_coords = [
        [[77, 313, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
        [[97, 313, 1, 0], [0, 0, 1, 0]],
        [[117, 313, 1, 0]],
        [[137, 313, 1, 0]],
        [[157, 313, 1, 0]],
        [[177, 313, 1, 0]]
    ]

    #setup locations for 4 door and 2 door, they will always be next to each other
    coord = 0 if door_coords[0][0][2] else 1
    for i in range(1, 4):
        door_coords[0][i][coord] = door_coords[0][i - 1][coord] + 2
        door_coords[0][i][coord^1] = door_coords[0][i - 1][coord^1]

    coord = 0 if door_coords[0][0][2] else 1
    door_coords[1][1][coord] = door_coords[1][0][coord] + 2
    door_coords[1][1][coord^1] = door_coords[1][0][coord^1]
    
    #print door_coords
    for i in xrange(7):
        for doorlist in door_coords[1:]:
            coord = 0 if doorlist[0][2] else 1
            for door in doorlist:
                door[coord] += 20
             
        # run simulations        
        start_time = time.time()
        main.run_simulation(door_coords, seed)
        end_time = time.time()

        print "Time taken: %f seconds"%(end_time - start_time)



if __name__ == '__main__':
    sim_runs()
